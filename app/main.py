from flask import Flask, render_template, redirect
import monclass

POKES = []

def setup_pokes():
    for i in range(1,53):
        suit = monclass.SUITS[i%4]
        val = monclass.VALS[i%13]
        pokemon=monclass.Pokemon(str(i), suit, val)
        POKES.append(pokemon)

