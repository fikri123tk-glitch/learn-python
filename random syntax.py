#!/usr/bin/env python3
"""
Sederhana: kalkulator kecil untuk belajar.

Fitur:
- Evaluasi ekspresi matematika sederhana (+ - * /, **, parentheses)
- REPL interaktif (ketik :q untuk keluar)
- Opsi CLI -e/--expr untuk evaluasi satu baris

File ini intentionally sederhana dan menggunakan ast untuk keamanan dasar
agar tidak langsung menjalankan kode arbitrary dengan eval().
"""
from __future__ import annotations

import ast
import operator
import argparse
import sys


_OPS = {
	ast.Add: operator.add,
	ast.Sub: operator.sub,
	ast.Mult: operator.mul,
	ast.Div: operator.truediv,
	ast.Pow: operator.pow,
	ast.Mod: operator.mod,
	ast.FloorDiv: operator.floordiv,
}


class CalcError(Exception):
	pass


def simple_eval(expr: str):
	"""Evaluasi ekspresi aritmetika sederhana dengan AST.

	Menerima angka, binary ops, unary +/- dan parentheses.
	"""
	try:
		node = ast.parse(expr, mode="eval")
	except SyntaxError as e:
		raise CalcError("Syntax error") from e

	def _eval(n):
		if isinstance(n, ast.Expression):
			return _eval(n.body)
		if isinstance(n, ast.Constant):
			if isinstance(n.value, (int, float)):
				return n.value
			raise CalcError("Unsupported constant")
		if isinstance(n, ast.Num):  # py<3.8
			return n.n  # type: ignore
		if isinstance(n, ast.BinOp):
			op_type = type(n.op)
			if op_type not in _OPS:
				raise CalcError(f"Operator tidak didukung: {op_type.__name__}")
			left = _eval(n.left)
			right = _eval(n.right)
			try:
				return _OPS[op_type](left, right)
			except Exception as e:
				raise CalcError(str(e))
		if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.UAdd, ast.USub)):
			val = _eval(n.operand)
			return +val if isinstance(n.op, ast.UAdd) else -val
		raise CalcError(f"Ekspresi tidak didukung: {type(n).__name__}")

	return _eval(node)


def repl():
	print("Kalkulator sederhana. Ketik :q untuk keluar.")
	while True:
		try:
			s = input("> ").strip()
		except (EOFError, KeyboardInterrupt):
			print()
			break
		if not s:
			continue
		if s == ":q":
			break
		try:
			res = simple_eval(s)
			print(res)
		except CalcError as e:
			print("Error:", e)


def main(argv=None):
	p = argparse.ArgumentParser(description="Kalkulator sederhana")
	p.add_argument("-e", "--expr", help="Evaluasi satu ekspresi dan keluar")
	args = p.parse_args(argv)
	if args.expr:
		try:
			print(simple_eval(args.expr))
			return 0
		except CalcError as e:
			print("Error:", e)
			return 2
	repl()
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
