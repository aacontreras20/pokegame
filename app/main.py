from flask import Flask, render_template, redirect
import monclass

POKES = []

def setup_pokes():

    ###put names code here pulling from api

    for i in range(1):
        suit = monclass.SUITS[i%4]
        val = monclass.VALS[i%13]
        pokemon=monclass.Pokemon(names[i], suit, val)
        POKES.append(pokemon)

