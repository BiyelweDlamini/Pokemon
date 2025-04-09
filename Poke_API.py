# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:56:21 2025

@author: biyel
"""
#imports the request module that has the needed functions
import requests as rq

pokeURL = "https://pokeapi.co/api/v2/"

#define our own function for getting pokemon information by typing in name

pokemonName = input("Enter the pokemon's name: ")

def getPokemonInfo(name):
    url = f"{pokeURL}/pokemon/{name}"
    response = rq.get(url)
    
    # This will return a HTTP status code, It should be 200 to mean that the response was okay
    
    print(f"This is the response code : {response}") 
    
    #print(response.status_code)
     
    # If statement to fetch data if the response code is equal to 200
    
    if response.status_code == 200:
        pokemonData = response.json()
        return pokemonData
    else:
        print(f"Failed to retrieve the data{response.status_code}")
        
    

info = getPokemonInfo(pokemonName)

if info:
    print(f"Pokemon_Name: {info['name']}")
    print(f"ID: {info['id']}")
    print(f"Height: {info['height']}")
