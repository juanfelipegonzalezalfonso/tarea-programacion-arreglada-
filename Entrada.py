{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN7tOMT8PWVv9S4nnsBBnaC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/juanfelipegonzalezalfonso/tarea-programacion-arreglada-/blob/entrada/Entrada.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mOUx_fY11VJ3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d6f982d1-2c0e-453f-d7c4-ba070e4c85d7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing entrada.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile entrada.py\n",
        "def ingresar_matriz():\n",
        "    while True:\n",
        "        try:\n",
        "            filas = int(input(\"Ingrese el número de filas: \"))\n",
        "            columnas = int(input(\"Ingrese el número de columnas: \"))\n",
        "            if filas > 0 and columnas > 0:\n",
        "                break\n",
        "            print(\"Dimensiones deben ser mayores a 0.\")\n",
        "        except ValueError:\n",
        "            print(\"Error: Ingrese números enteros.\")\n",
        "\n",
        "    matriz = []\n",
        "    for i in range(filas):\n",
        "        while True:\n",
        "            try:\n",
        "                fila = list(map(float, input(f\"Ingrese la fila {i+1} separada por espacios: \").split()))\n",
        "                if len(fila) != columnas:\n",
        "                    print(f\"Error: debe ingresar exactamente {columnas} valores.\")\n",
        "                else:\n",
        "                    matriz.append(fila)\n",
        "                    break\n",
        "            except ValueError:\n",
        "                print(\"Error: Ingrese solo números.\")\n",
        "    return matriz\n",
        "\n",
        "def mostrar_matriz(matriz):\n",
        "    for fila in matriz:\n",
        "        print(fila)"
      ]
    }
  ]
}