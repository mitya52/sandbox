class Ratio():
	'''
		Rational numbers implementation
	'''
	def __init__(self, p=0, q=1):
		if type(p) != int or type(q) != int:
			raise TypeError('p and q must be integer')
		if q <= 0:
			raise ValueError('q must be > 0')
		self.p = p
		self.q = q
		self._normalize()

	# Arithmetic operators
	def __mul__(self, other):
		if type(other) == Ratio:
			return Ratio(self.p*other.p, self.q*other.q)
		if type(other) == int:
			return Ratio(self.p*other, self.q)
		self._rise_invalid_type(other)

	__rmul__ = __mul__
	__imul__ = __mul__

	def __add__(self, other):
		if type(other) == Ratio:
			return Ratio(self.p*other.q + self.q*other.p, self.q*other.q)
		if type(other) == int:
			return Ratio(self.p + self.q*other, self.q)
		self._rise_invalid_type(other)

	__radd__ = __add__
	__iadd__ = __add__

	def __truediv__(self, other):
		if type(other) == Ratio:
			if other.p == 0:
				raise ValueError('division by zero')
			return Ratio(self.p*other.q, other.p*self.q)
		if type(other) == int:
			if other == 0:
				raise ValueError('division by zero')
			return Ratio(self.p, self.q*other)
		self._rise_invalid_type(other)

	__floordiv__ = __truediv__
	__itruediv__ = __truediv__
	__ifloordiv__ = __truediv__

	def __rtruediv__(self, other):
		if self.p == 0:
			raise ValueError('division by zero')
		if type(other) == Ratio:
			return Ratio(self.q*other.p, other.q*self.p)
		if type(other) == int:
			return Ratio(self.q*other, self.p)
		self._rise_invalid_type(other)

	__rfloordiv__ = __rtruediv__

	def __sub__(self, other):
		if type(other) == Ratio:
			return Ratio(self.p*other.q - other.p*self.q, self.q*other.q)
		if type(other) == int:
			return Ratio(self.p - other*self.q, self.q)
		self._rise_invalid_type(other)

	__isub__ = __sub__

	def __rsub__(self, other):
		if type(other) == Ratio:
			return Ratio(self.q*other.p - self.p*other.q, self.q*other.q)
		if type(other) == int:
			return Ratio(self.q*other - self.p, self.q)
		self._rise_invalid_type(other)

	def __neg__(self):
		self.p = -self.p
		return self

	def __pos__(self):
		return self

	def __abs__(self):
		self.p = abs(self.p)
		return self

	def __pow__(self, power):
		if type(power) == int:
			return Ratio(self.p**power, self.q**power)
		raise TypeError('invalid operand type "{}", must be int'.format(type(power)))

	# Logic operators
	def __lt__(self, other):
		if type(other) == int:
			other = Ratio(other)
		if type(other) == Ratio:
			return (other - self).p > 0
		self._rise_invalid_type(other)

	def __le__(self, other):
		return not (self < other)

	def __gt__(self, other):
		return not (self <= other)

	def __ge__(self, other):
		return not (self > other)

	def __eq__(self, other):
		return not (self < other or other < self)

	def __ne__(self, other):
		return not (self == other)

	# Cast operators
	def __int__(self):
		return self.p // self.q

	def __float__(self):
		return float(self.p) / self.q

	def __bool__(self):
		return self != 0

	def __str__(self):
		return '{} / {}'.format(self.p, self.q)

	# Methods for inner usage
	def _normalize(self):
		from math import gcd
		from numpy import sign

		if self.q == 0:
			assert('This cannot happens')
		if self.p == 0:
			self.q = 1
			return
		g = gcd(abs(self.q), abs(self.p))
		s = sign(self.p * self.q)
		self.p = int(abs(self.p) // g * s)
		self.q = int(abs(self.q) // g)

	def _rise_invalid_type(self, other):
		raise TypeError('invalid operand type "{}", valid types: Ratio, int'.format(type(other)))

if __name__ == '__main__':
	a = int(1.1*1e38) # very large number

	# use float
	b = 1 / a
	print(int(b * a))

	# use Ratio
	b = Ratio(1) / a
	print(int(b * a))