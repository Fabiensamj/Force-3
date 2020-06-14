# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:34:50 2020

@author: Menudier, Sam, Benis
"""

##ce code permet de faire l'executable
from cx_Freeze import setup, Executable

setup(
      name = "Force 3",
      version = "0.1",
      description = "Jouer à force 3 avec une IA",
      executables = [Executable("Accueil.py")]
      )