# -*- encoding: utf-8 -*-

import codecs
import re
from fmatrixutils import find_pos, find_neg
from constants import  ( IPA_SYMBOLS, STRESS, VOWELLS, CONSONANTS, PERIOD, COMMA, SYLLABLE, 
							FMATRIX, GLIDES, VOWELLS_GLIDES, LIQUIDS, NASALS, NASALS_LIQUIDS,
							AFFRICATES, LARYNGEALS, NONCORONAL_OBSTRUENTS, PALATAL_OBSTRUENTS,
							CORONAL_OBSTRUENTS, DISTINCTIVE_FEATURES, FEATURE_GROUPS )


class BasePhonologist( object ):
	"""
	Base class with magic methods for all other classes.
	"""
	def __init__( self, tokens ):
		self.tokens = InputManager(tokens).words()		

	def __len__( self ):
		return len(self.tokens)

	def __iter__( self ):
		return TokenIterator( self.tokens )

	def __getitem__( self, ndx ):
		assert ndx >= 0 and ndx < len( self.tokens ), "index out of range"
		return self.tokens[ ndx ]

	def __setitem__( self, ndx, token ):
		assert ndx >= 0 and ndx < len( self.tokens ), "index out of range"
		self.tokens[ ndx ] = token


######################################################
class BaseTokens( BasePhonologist ):
	"""
	This is a base class for Words and Syllables (the "tokens" classes). 
	Words objects should be divided at word boundries.
	Syllables objects should be divided at syllable boundries.
	"""

	def count_token( self, target ):
		"""
		Count the frequency of target token.
		----------------------
		target - word or syllable
		return - dict { token : frequency }
		"""
		target = InputManager( target ).force_unicode()
		token_dict = { target: 0 }
		for token in self.tokens:
			if token == target:
				token_dict[ target ] += 1
		return token_dict

	def preceding_token( self, target ):
		"""
		Count the frequency of tokens preceding target token.
		-----------------------
		target - word or syllable
		return - dict { target token : frequency }
		"""
		target = InputManager(target).force_unicode()
		token_dict = {}
		for ndx, token in enumerate(self.tokens[ 1: ]):
			if token == target:
				token_dict.setdefault( self.tokens[ ndx ], 0 )
				token_dict[ self.tokens[ ndx ] ] += 1
		return token_dict 

	def posterior_token( self, target ):
		"""
		Count the frequency of tokens posterior to target token.
		-----------------------
		target - word or syllable
		return - dict { posterior token : frequency }
		"""
		target = InputManager(target).force_unicode()
		token_dict = {}
		ndx = 0
		for i in range( len( self.tokens ) - 1 ):
			if self.tokens[ndx] == target:
				token_dict.setdefault( self.tokens[ ndx + 1], 0 )
				token_dict[ self.tokens[ndx + 1] ] += 1
			ndx += 1
		return token_dict

	def stressed_frequency( self ):
		"""
		Count the frequency of all tokens containing primary stress.
		---------------------
		return - dict { word with primary stress : frequency }
		"""
		stress_dict = {}
		for token in self.tokens:
			if STRESS in token:
				stress_dict.setdefault( token, 0 )
				stress_dict[ token ] += 1
		return stress_dict

	def unstressed_frequency( self ):
		"""
		Count the frequency of all tokens not containing primary stress.
		---------------------
		return - dict { word without primary stress : frequency }
		"""
		stress_dict = {}
		for token in self.tokens:
			if STRESS not in token:
				stress_dict.setdefault( token, 0 )
				stress_dict[ token ] += 1
		return stress_dict

	def token_by_symbol( self, target ):
		"""
		Count the frequency of all tokens containing a particular syllable.
		---------------------
		target - ipa symbol
		return - dict { token with symbol : frequency }
		"""
		target = InputManager( target ).force_unicode()
		token_dict = {}
		for token in self.tokens:
			if target in token:
				token_dict.setdefault( token, 0 )
				token_dict[ token ] += 1
		return token_dict
	
	def stressed_token_by_symbol( self, target ):
		"""
		Count the frequency of stressed tokens containing a particular symbol.
		---------------------
		target - ipa symbol
		return - dict { stressed token with symbol : frequency }
		"""
		target = InputManager( target ).force_unicode()
		tokens = self.token_by_symbol( target )
		token_dict = {}
		for token in tokens.keys():
			if STRESS in token:
				token_dict.setdefault(token,0)
				token_dict[ token ] += tokens[token]
		return token_dict

	def unstressed_token_by_symbol( self, target ):
		"""
		Count the frequency of unstressed tokens containing a particular symbol.
		---------------------
		target - ipa symbol
		return - dict { unstressed token with symbol : frequency }
		"""
		target = InputManager( target ).force_unicode()
		tokens = self.token_by_symbol( target )
		token_dict = {}
		for token in tokens.keys():
			if STRESS not in token:
				token_dict.setdefault(token,0)
				token_dict[ token ] += tokens[token]
		return token_dict

	def syllabify( self ):
		"""
		Break a "Words" format object into syllables.
		--------------------
		return - list [ syll, ..., syll ]
		"""
		syllables = []
		for token in self.tokens:
			syllables.append(token.split("."))
		return sum(syllables,[]) # hehe good trick

	def _stressed( self, token ):
		"""
		Check token for primary stressed. Currently only used once, could be used more.
		May get rid of this.
		"""
		if STRESS in token:
			return True
		else:
			return False

class Phrases( BaseTokens ):
	"""
	May create Phrases class.
	"""
	pass

	def pretonic_postonic_phrases(self):
		pass

##############################################################
class Words( BaseTokens ):
	"""
	Class for working with tokens divided at word boundries
	"""

	@classmethod
	def loadfile( Words, ipa_textfile ):
		"""
		Try to read the input textfile to proper format for words.
		"""
		f = codecs.open( ipa_textfile, "r", encoding='utf-8' )
		text = f.readline()
		words = text.split()
		f.close()
		return Words(words)
	
	def pretonic_postonic_words( self, target ):
		"""
		Currently just counts the occurence of a symbol in a pretonic
		or postonic position taking into account word boundries.
		----------------------
		target - ipa symbol 
		return dict { pretonic : frequency, postonic : frequency }
		"""
		target = InputManager(target).force_unicode()
		count_dict = { "pretonic":0, "postonic":0 }
		for token in self.tokens:
			if target in token:
				token_dict = self._pretonic_postonic( target, token )
				count_dict[ "pretonic" ] += token_dict[ "pretonic" ]
				count_dict[ "postonic" ] += token_dict[ "postonic" ]
					
		return count_dict
	
	def _pretonic_postonic( self, target, token ):
		"""
		Counts pretonic postonic per word.
		"""
		count_dict = { "pretonic":0, "postonic":0 }
		stoken = token.split( "." )
		if len( stoken ) > 1:
			for ndx, syll in enumerate( stoken ):
				if target in syll and not self._stressed( syll ):
					if ndx > 0 and STRESS in stoken[ ndx-1 ]:
						count_dict[ "pretonic" ] += 1
					if ndx < len( stoken ) - 1 and STRESS in stoken[ ndx+1 ]:
						count_dict[ "postonic" ] += 1			
			return count_dict
		else:
			return count_dict

###################################################
class Syllables( BaseTokens ):
	"""
	Class for working with tokens divided at syllable boundries.
	"""

	@classmethod
	def loadfile( Syllables, ipa_textfile ):
		"""
		Try to read textfile input to proper format for syllables.
		"""
		f = codecs.open( ipa_textfile, "r", encoding='utf-8')
		text = f.readline()
		tokens = text.split()
		syllable_list = []
		for word in tokens:
			syllable_list.append(word.split("."))
		syllables = sum(syllable_list,[])
		return Syllables(syllables)

	def __init__( self, tokens ):
		self.tokens = InputManager(tokens).syllables()

	def pretonic_postonic_syllables(self):
		pass

	#### SYLLABLE NUCLEUS AND EVERYTHING HERE i.e. More Methods Coming

###############################################################
class Symbols( BasePhonologist ):
	"""
	Class for working with transcriptions at a symbol level.
	Does not take into account syllable or word boundries.
	May be merged with the Features class.
	"""
	### CLASS ATTRIBUTE ###
	# This is a list of groups that can be passed through various methods.
	# Need to change the format for clean passing... 
	feature_groups = FEATURE_GROUPS

	@classmethod
	def loadfile( Symbols, ipa_textfile ):
		"""
		Try to read textfile to proper format for Symbols.
		"""
		f = codecs.open( ipa_textfile, "r", encoding='utf-8')
		text = f.readline()
		joined_text = re.sub( '\s', '', text )
		syllables = joined_text.split( "." )
		symbols = ''.join( syllables )
		return Symbols( symbols )
		
	def __init__( self, tokens ):
		self.tokens = InputManager( tokens ).symbols()

	def count_symbol( self, target ):
		"""
		Count the frequency of a particular symbol.
		---------------------
		target - ipa symbol
		return - dict { symbol : frequency }
		"""
		pass

	def preceding_symbol( self, target  ):
		"""
		Count the frequency of symbols preceding the target.
		---------------------
		target - ipa symbol
		return - dict { symbol : frequency }
		"""
		target = InputManager(target).force_unicode()
		count_dict = {}
		for ndx,symbol in enumerate( self.tokens[ 1:] ):
			if symbol == target:
				if STRESS != self.tokens[ndx]: 
					count_dict.setdefault( self.tokens[ ndx ],0 )
					count_dict[self.tokens[ ndx ]] += 1
				elif ndx > 0:
					count_dict.setdefault( self.tokens[ ndx - 1 ],0 )
					count_dict[self.tokens[ ndx - 1 ]] += 1
		return count_dict

#####################################################################################
# THESE METHODS WILL PROBABLY BE REPLACED BY AN OPTIONAL VARIABLE IN preceding_symbol
# OR A METHOD proceeding_feature_groups
#####################################################################################
	def preceding_consonant( self, target ):
		target = InputManager(target).force_unicode()
		count_dict = {}
		for ndx,symbol in enumerate( self.tokens[ 1:] ):
			if symbol == target:
				if STRESS != self.tokens[ndx]: 
					if self.tokens[ ndx ] in CONSONANTS:
						count_dict.setdefault( self.tokens[ ndx ],0 )
						count_dict[self.tokens[ ndx ]] += 1
				elif ndx > 0 and self.tokens[ ndx - 1 ] in CONSONANTS:
					count_dict.setdefault( self.tokens[ ndx - 1 ],0 )
					count_dict[self.tokens[ ndx - 1 ]] += 1
		return count_dict

	def preceding_vowell( self, target ):
		target = InputManager(target).force_unicode()
		count_dict = {}
		for ndx,symbol in enumerate( self.tokens[ 1:] ):
			if symbol == target:
				if STRESS != self.tokens[ndx]: 
					if self.tokens[ ndx ] in VOWELLS:
						count_dict.setdefault( self.tokens[ ndx ],0 )
						count_dict[self.tokens[ ndx ]] += 1
				elif ndx > 0 and self.tokens[ ndx - 1 ] in VOWELLS:
					count_dict.setdefault( self.tokens[ ndx - 1 ],0 )
					count_dict[self.tokens[ ndx - 1 ]] += 1
		return count_dict
##########################################################################

	def posterior_symbol( self, target ):
		"""
		Count the frequency of symbols preceding the target.
		---------------------
		target - ipa symbol
		return - dict { symbol : frequency }
		"""
		target = InputManager(target).force_unicode()
		count_dict = {}
		ndx = 0
		for i in range( len( self.tokens ) - 1):
			if self.tokens[ndx] == target:
				if STRESS != self.tokens[ndx+1]:
					count_dict.setdefault( self.tokens[ ndx + 1 ],0 )
					count_dict[self.tokens[ ndx + 1 ]] += 1
				else:
					count_dict.setdefault( self.tokens[ ndx + 2 ],0 )
					count_dict[self.tokens[ ndx + 2 ]] += 1						
			ndx += 1
		return count_dict	

#####################################################################################
# THESE METHODS WILL PROBABLY BE REPLACED BY AN OPTIONAL VARIABLE IN posterior_symbol
# OR A METHOD posterior_feature_groups
#####################################################################################
	def posterior_consonant( self, target ):
		target = InputManager(target).force_unicode()
		count_dict = {}
		ndx = 0
		for i in range( len( self.tokens ) - 1):
			if self.tokens[ndx] == target:
				if STRESS != self.tokens[ndx+1]:
					if self.tokens[ ndx + 1] in CONSONANTS:
						count_dict.setdefault( self.tokens[ ndx + 1 ],0 )
						count_dict[self.tokens[ ndx + 1 ]] += 1
				elif self.tokens[ndx + 2] in CONSONANTS:
					count_dict.setdefault( self.tokens[ ndx + 2 ],0 )
					count_dict[self.tokens[ ndx + 2 ]] += 1						
			ndx += 1
		return count_dict	

	def posterior_vowell( self, target ):
		target = InputManager(target).force_unicode()
		count_dict = {}
		ndx = 0
		for i in range( len( self.tokens ) - 1):
			if self.tokens[ndx] == target:
				if STRESS != self.tokens[ndx+1]:
					if self.tokens[ ndx + 1] in VOWELLS:
						count_dict.setdefault( self.tokens[ ndx + 1 ], 0 )
						count_dict[self.tokens[ ndx + 1 ]] += 1
				elif self.tokens[ ndx + 2] in VOWELLS:
					count_dict.setdefault( self.tokens[ ndx + 2 ], 0 )
					count_dict[self.tokens[ ndx + 2 ]] += 1
			ndx += 1
		return count_dict	

##################################################################
class Features( Symbols ):
	"""
	Class for working with distinctive features at the symbol level.
	May be merged with Symbols class.
	"""
	### Class attributes for reference ###
	# possible features for use with features method
	features_dictionary = DISTINCTIVE_FEATURES

	@classmethod
	def loadfile( Symbols, ipa_textfile ):
		"""
		Same loadfile. Different return - Features class.
		"""
		f = codecs.open( ipa_textfile, "r", encoding='utf-8' )
		text = f.readline()
		joined_text = re.sub('\s', '', text)
		syllables = joined_text.split(",")
		symbols = ''.join(syllables)
		return Features(symbols)
		
	def features( self, plus=None, minus=None ):
		"""
		Find all symbols with a series of feature characteristics as 
		defined by plus and minus.
		--------------------------
		plus - a list of distinctive features with positive value
		minus - a list of distinctive features with negative value
		return set ([ sym, ..., sym ])
		"""
		if plus:
			if minus:
				data = self.find_plus( plus )
				return self.find_minus( minus, data_arg=data )
			else:
				return self.find_plus( plus )
		else:
			return self.find_minus( minus )

	def find_plus( self, plus, data_arg=None ):
		"""
		Find all symbols with a series of feature characteristics as 
		defined by plus.
		--------------------------
		plus - a list of distinctive features with positive value
		return set ([ sym, ..., sym ])
		"""
		assert type( plus ) == list, "plus must be passed as list [ ] "
		ndx = len( plus ) - 1
		if data_arg:
			data = list( data_args )
		else:
			data = self.tokens
		for feature in plus:
			n_data = find_pos( feature, data ) #from fmatrix_utils
			data = n_data
		output = set( data )
		return output

	def find_minus( self, minus, data_arg=None ):
		"""
		Find all symbols with a series of feature characteristics as 
		defined by minus.
		--------------------------
		minus - a list of distinctive features with positive value
		return set ([ sym, ..., sym ])
		"""
		assert type( minus ) == list, "minus must be passed as list [ ] "
		ndx = len( minus ) - 1
		if data_arg:
			data = list( data_arg )
		else:
			data = self.tokens
		for feature in minus:
			n_data = find_neg( feature, data ) #from fmatrix_utils
			data = n_data
		output = set( data )
		return output

	def feature_group( self, group ): #INVENTORY
		"""
		Count the frequency of all symbols in transcription 
		based on their distinctive feature grouping.
		---------------------
		group - a distinctive features group
		return - dict { symbol : frequency }
		"""
		symbol_dict = {}
		for symbol in self.tokens:
			if symbol in group:
				symbol_dict.setdefault( symbol, 0 )
				symbol_dict[ symbol ] += 1
		return symbol_dict

	def features_in_common( self, *targets ):
		"""
		Determine what features two or more have in
		common.
		"""
		pass 

class Vowels( Features ):
	"""
	Probably be part of features. Vowel featurmatrix etc.
	"""
	pass

#######################################################
class TokenIterator( object ):
	def __init__( self, phon_trans  ):
		self.current = 0
		self._token_ref = phon_trans

	def __iter__( self ):
		return self

	def next( self ):
		if self.current < len( self._token_ref ):
			token = self._token_ref[ self.current ]
			self.current += 1
			return token
		else:
			raise StopIteration

class InputManager( object ):
	"""
	Strange class. I don't know if this is out of the
	ordinary. I want to make sure user input comes in 
	the right format so I made a class to deal with it.
	"""

	def __init__(self, input):
		self.input = input

	def force_unicode(self):
		if type(self.input) == str:
			return self.input.decode('utf-8')
		else:
			return self.input

	def words( self ):
		if type(self.input) == list:
			return self.input
		elif type(self.input) == unicode:
			return self.input.split()
		elif type(self.input) == str:
			uinput = self.input.decode('utf-8')
			return uinput.split()
		else:
			raise TypeError

	def syllables( self ):
		if type(self.input) == Words or type(self.input) == Phrases: 
			return self.input.syllabify()
		elif type(self.input) == list:
			return self.input
		elif type(self.input) == unicode:
			return self.input.split(".")
		elif type(self.input) == str:
			uinput = self.input.decode('utf-8')
			return uinput.split(".")
		else:
			raise TypeError

	def symbols( self ):
		if type(self.input) == Words or type(self.input) == Phrases:
			return ''.join( self.input.syllabify() )
		elif type(self.input) == Syllables:
			return ''.join( self.input.tokens )
		elif type(self.input) == unicode:
			output = re.sub( '\s','', self.input )
			return output
		if type(self.input) == str:
			output = re.sub('\s','', self.input)
			return output.decode('utf-8')
		elif type(self.input) == list:
			return ''.join(self.input)
		else:
			raise TypeError


	




