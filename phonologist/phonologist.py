# -*- encoding: utf-8 -*-

import codecs
import re
from fmatrixutils import *
from utils import force_unicode, load_file
from constants import   IPA_SYMBOLS, STRESS, VOWELLS, CONSONANTS, PERIOD, COMMA, SYLLABLE, FMATRIX

#### Object oriented library for working with IPA transcriptions. ####

#### Class to create the Phonetic Transcription Object. ####
class Phonologist( object ):
	"""
	base class
	"""
	def __init__( self, tokens ):
		if type(tokens) == list:
			self.tokens = tokens
		else:
			self.tokens = InputMng(tokens).words()		
			
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
class Tokens( Phonologist ):
	"""
	this is a base class for Words and Syllables
	"""

	@classmethod
	def loadfile( Words, ipa_txtfile ):
		tokens = load_file( ipa_txtfile )
		return Tokens(tokens)

	def target_token( self, target_token ):
		target_token = force_unicode( target_token )
		count_dict = {}
		for token in self.tokens:
			if token == target_token:
				count_dict.setdefault( token, 0 )
				count_dict[token] += 1
		return count_dict

	def preceding_token( self, target ):
		target = force_unicode( target )
		count_dict = {}
		for ndx, token in enumerate(self.tokens[ 1: ]):
			if token == target:
				print token 
				count_dict.setdefault( self.tokens[ ndx ], 0 )
				count_dict[ self.tokens[ ndx ] ] += 1
		return count_dict 

	def posterior_token( self, target ):
		target = force_unicode( target )
		count_dict = {}
		ndx = 0
		for i in range( len( self.tokens ) - 1 ):
			if self.tokens[ndx] == target:
				count_dict.setdefault( self.tokens[ ndx + 1], 0 )
				count_dict[ self.tokens[ndx + 1] ] += 1
			ndx += 1
		return count_dict

	def stressed_frequency( self ):
		stress_dict = {}
		for token in self.tokens:
			for char in token:
				if char == STRESS:
					stress_dict.setdefault( token, 0 )
					stress_dict[ token ] += 1
		return stress_dict

	def unstressed_frequency( self ):
		stress_dict = {}
		for token in self.tokens:
			if STRESS not in token:
				stress_dict.setdefault( token, 0 )
				stress_dict[ token ] += 1
		return stress_dict

	def syllabify( self ):
		syllables = []
		for token in self.tokens:
			syllables.append(token.split("."))
		return sum(syllables,[]) # hehe good trick

	# GEN
	def _stressed( self, token ):
		if STRESS in token:
			return True
		else:
			return False

	# Count stress in a token
	def stressed_per_token(self):
		return 

	def unstressed_per_token(self):
		return 
class Phrases( object ):
	pass

##############################################################
class Words( Tokens ):

	@classmethod
	def loadfile( Words, ipa_txtfile ):
		tokens = load_file( ipa_txtfile )
		return Words(tokens)
	
	def return_token_words( self, target ):
		count_dict = {}
		for token in self.tokens:
			for sym in token:
				if sym.encode('utf-8') in target:
					count_dict.setdefault( token, 0 )
					count_dict[token] += 1
					break
		return count_dict
	
	def stressed_target_words( self, target ):
		### faster if I don't call return tokens
		tokens = self.return_tokens_words( target )
		count_dict = {}
		for token in tokens.keys():
			if STRESS in token:
				count_dict.setdefault(token,0)
				count_dict[ token ] += tokens[token]
		return count_dict

	def unstressed_target_words( self, target ):
		### faster if I don't call return tokens
		tokens = self.return_tokens_words( target )
		count_dict = {}
		for token in tokens.keys():
			if STRESS not in token:
				count_dict.setdefault(token,0)
				count_dict[ token ] += tokens[token]
		return count_dict

	def pretonic_postonic_words( self, target ):
		target = force_unicode( target )
		count_dict = {"pretonic":0,"postonic":0}
		for token in self.tokens:
			for sym in token:
				if sym == target:
					token_dict = self._pretonic_postonic(target,token)
					count_dict["pretonic"] += token_dict["pretonic"]
					count_dict["postonic"] += token_dict["postonic"]
					break
		return count_dict
	
	def _pretonic_postonic( self, target, token ):
		### Don't like all of this trying
		count_dict = {"pretonic":0,"postonic":0}
		stoken = token.split(".")
		if len(stoken) > 1:
			for ndx, syll in enumerate( stoken ):
				if not self._stressed(syll):
					for sym in syll:
						if sym in target:
							if ndx > 0 and STRESS in stoken[ndx-1]:
								count_dict["pretonic"] += 1
							if ndx < len(stoken) - 1 and STRESS in stoken[ndx+1]:
								count_dict["postonic"] += 1			
			return count_dict
		else:
			return count_dict

###################################################
class Syllables( Tokens ):

	@classmethod
	def loadfile( Syllables, ipa_txtfile ):
		ftokens = load_file( ipa_txtfile )
		ltokens = []
		for token in ftokens:
			ltokens.append(token.split("."))
		tokens = sum(ltokens,[])
		return Syllables(tokens)

	def __init__( self, tokens ):
		if type(tokens) == Words or type(tokens) == Phrases: 
			self.tokens = tokens.syllabify()
		elif type(tokens) == list:
			self.tokens = tokens
		else:
			self.tokens = InputMng(tokens).syllables()


	def return_token_sylls( self, target ):
		targ = force_unicode( target )
		count_dict = {}
		for token in self.tokens:
			print token
			for sym in token:
				if sym == target:
					count_dict.setdefault( token, 0 )
					count_dict[token] += 1
		return count_dict
	
	def stressed_target_sylls( self, target ):
		### faster if I don't call return tokens
		tokens = self.return_tokens_sylls( target )
		count_dict = {}
		for token in tokens.keys():
			if STRESS in token:
				count_dict.setdefault(token,0)
				count_dict[ token ] += tokens[token]
		return count_dict

	def unstressed_target_sylls( self, target ):
		### faster if I don't call return tokens
		tokens = self.return_tokens_sylls( target )
		count_dict = {}
		for token in tokens.keys():
			if STRESS not in token:
				count_dict.setdefault(token,0)
				count_dict[ token ] += tokens[token]
		return count_dict

###############################################################
class Symbols( Phonologist ):

	@classmethod
	def loadfile( Symbols, ipa_txtfile ):
		ftokens = load_file( ipa_txtfile )
		jtokens = ''.join(ftokens)
		stokens = jtokens.split(".")
		tokens = ''.join(stokens)
		return Symbols(tokens)

	def __init__( self, tokens ):
		if type(tokens) == Words:
			self.tokens = ''.join( tokens.syllabify() )
		elif type(tokens) == Syllables:
			self.tokens = ''.join( tokens.tokens )
		elif type(tokens) == unicode:
			output = re.sub( '\s','', tokens )
			self.tokens = output
		else:
			self.tokens = InputMng(tokens).symbols()


	def preceding_symbol( self, target  ):
		target = force_unicode( target )
		count_dict = {}
		for ndx,symbol in enumerate( self.tokens[ 1:] ):
			if symbol == target:
				count_dict.setdefault( self.tokens[ ndx ],0 )
				count_dict[self.tokens[ ndx ]] += 1
		return count_dict

	def preceding_consonant( self, target ):
		target = force_unicode( target )
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
		target = force_unicode( target )
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

	def posterior_symbol( self, target ):
		target = force_unicode( target )
		count_dict = {}
		ndx = 0
		for i in range( len( self.tokens ) - 1):
			if self.tokens[ndx] == target:
				count_dict.setdefault( self.tokens[ ndx + 1 ],0 )
				count_dict[self.tokens[ ndx + 1 ]] += 1
			ndx += 1
		return count_dict	

	def posterior_consonant( self, target ):
		target = force_unicode( target )
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
		target = force_unicode( target )
		count_dict = {}
		ndx = 0
		for i in range( len( self.tokens ) - 1):
			if self.tokens[ndx] == target:
				if STRESS != self.tokens[ndx+1]:
					if data[ ndx + 1] in VOWELLS:
						count_dict.setdefault( data[ ndx + 1 ], 0 )
						count_dict[data[ ndx + 1 ]] += 1
				elif data[ ndx + 2] in VOWELLS:
					count_dict.setdefault( data[ ndx + 2 ], 0 )
					count_dict[data[ ndx + 2 ]] += 1
			ndx += 1
		return count_dict	

class Features( Symbols ):

	@classmethod
	def loadfile( Features, ipa_txtfile ):
		ftokens = load_file( ipa_txtfile )
		jtokens = ''.join(ftokens)
		stokens = jtokens.split(".")
		tokens = ''.join(stokens)
		return Features(tokens)

	def features(self, posfeatures=None, negfeatures=None ):
		return posfeatures,negfeatures
	def vowels( self ):
		return 
	def glides( self ):
		return 
	def nasals( self ):
		return 
	def liquids( self ):
		return 
	def affricates( self ):
		return 
	def laryngeals( self ):
		return 
	def noncoronal_obstruents( self ):
		return 
	def palatal_obstruents( self ):
		return 
	def coronal_obstruents( self ):
		return


#### Iterator class. ####
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

class InputMng( object ):

	def __init__(self, input):
		self.input = input

	def words( self ):
		if type(self.input) == unicode:
			return self.input.split()
		elif type(self.input) == str:
			uinput = self.input.decode('utf-8')
			return uinput.split()
		else:
			raise TypeError, "available"

	def syllables( self ):
		if type(self.input) == unicode:
			return self.input.split(".")
		elif type(self.input) == str:
			uinput = self.input.decode('utf-8')
			return uinput.split(".")
		else:
			raise TypeError

	def symbols( self ):
		if type(self.input) == str:
			output = re.sub('\s','', self.input)
			return output.decode('utf-8')
		elif type(self.input) == list:
			return ''.join(self.input)
		else:
			raise TypeError







