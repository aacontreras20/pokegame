from flask import Flask, render_template, redirect
from monclass import SUITS, VALS, Pokemon, ApiURLopener

POKES = []

def setup_pokes():
    for i in range(1,53):
        suit = SUITS[i%4]
        val = VALS[i%13]
        pokemon=Pokemon(str(i), suit, val)
        POKES.append(pokemon)

