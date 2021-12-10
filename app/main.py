from flask import flask, render_template, redirect
import monclass

POKES = []

def setup_pokes():
    names = []
    for i in range(52):
        suit = monclass.SUITS[i%4]
        val = monclass.VALS[i%13]
        pokemon=monclass.Pokemon(names[i], suit, val)
        POKES.append(pokemon)

