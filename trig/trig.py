#!/usr/bin/env python3.12

"""
Filename:		trig.py
Date:			2026.04.04
Author:			Tristan McGuire
Description:	Remembering how trigonometry works.
License: 		Copyright 2026 Tristan McGuire

				Redistribution and use in source and binary forms, with or without modification, are permitted 
				provided that the following conditions are met:

					1. Redistributions of source code must retain the above copyright notice, this list of conditions 
					   and the following disclaimer.

					2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions 
					   and the following disclaimer in the documentation and/or other materials provided with the distribution.

					3. Neither the name of the copyright holder nor the names of its contributors may be used to 
					   endorse or promote products derived from this software without specific prior written permission.

				THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED 
				WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
				PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR 
				ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED 
				TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
				HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
				NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
				OF SUCH DAMAGE.
"""

import math


def pythag(adj: float = None, opp: float = None, hyp: float = None) -> list:
	sides = [opp, adj, hyp]
	missing_side = -1

	for index, side in enumerate(sides):
		if side == None:
			missing_side = index
			break

	if missing_side == 2:
		sides[2] = math.sqrt((sides[0]**2) + (sides[1]**2))

	if missing_side == 1: 
		sides[1] = math.sqrt((sides[2]**2) - (sides[0]**2))

	if missing_side == 0:
		sides[0] = math.sqrt((sides[2]**2) - (sides[1]**2))

	return sides


def rt_angles(A: float = None, O: float = None, H: float = 90.0, sides: list = [None,None,None]) -> list[float, float, float]:
	pass


def sin_theta(opp: float, hyp: float) -> float:
	return opp/hyp


def cos_theta(adj: float, hyp: float) -> float:
	return adj/hyp


def tan_theta(opp: float, adj: float) -> float:
	return opp/adj


def cot_theta(adj: float, opp: float) -> float:
	return adj/opp


def sec_theta(hyp: float, adj: float) -> float:
	return hyp/adj


def csc_theta(hyp: float, opp: float) -> float:
	return hyp/opp


def radians_to_degrees(radians: float) -> float:
	return (180 / math.pi) * radians


def degrees_to_radians(degrees: int) -> float:
	return math.pi/180.0 * degrees


if __name__ == "__main__":
	adj = 6.7
	opp = 4.5
	sides = pythag(adj = adj, opp = opp, hyp = None)
	hyp = sides[2]

	sin_theta = sin_theta(opp, hyp)					# soh
	cos_theta = cos_theta(adj, hyp)					# cah
	tan_theta = tan_theta(opp, adj)					# toa
	cot_theta = cot_theta(adj, opp)					# cao - reciprocal of toa (tangent)
	sec_theta = sec_theta(hyp, adj)					# sha - reciprocal of cah (cosine)
	csc_theta = csc_theta(hyp, opp)					# cho - reciprocal of soh (sine)

	theta_radians = math.acos(((sides[1]**2) + (sides[2]**2) - (sides[0]**2)) / (2 * sides[1] * sides[2]))
	theta_degrees = theta_to_degrees(theta_radians)

	print(f"\n{'='*100}")
	print(f"Hypotenuse: {hyp}\n")
	print(f"Theta (Degrees):\t{theta_degrees},\t||\tTheta (Radians):\t{theta_radians}")
	print(f"\n{'='*100}")
	print(f"Sin Theta:\t\t{sin_theta},\t||\tCosine Theta:\t\t{cos_theta}")
	print(f"Tangent Theta:\t\t{tan_theta},\t||\tCotangent Theta:\t{cot_theta}")
	print(f"Secant Theta:\t\t{sec_theta},\t||\tCosecant Theta:\t\t{csc_theta}")
	print()

	for x in range(0, 361, 10):
		radians = degrees_to_radians(x)

		sin_value = math.sin(radians)
		cos_value = math.cos(radians)
		
		if math.fabs(sin_value) < 0.0009:
			sin_value = 0.00  					# This cleans up a ridiculously small value being returned at 
												# the 0 crossing between positive and negative values for the 
												# final 90 degrees of the wave.

		print(f"Degrees: {x}\t||\tSine: {sin_value:.4f}\t||\tCosine: {cos_value:.4f}")

