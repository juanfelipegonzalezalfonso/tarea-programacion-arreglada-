{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN1Q6acu/cbf8jRgyvf4WLN",
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
        "<a href=\"https://colab.research.google.com/github/juanfelipegonzalezalfonso/tarea-programacion-arreglada-/blob/operaciones/operaciones.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gszYF-3D5jpf",
        "outputId": "fbe3427f-48c1-4c98-93b1-9165b81d22bf"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing operaciones.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile operaciones.py\n",
        "def sumar_matrices(A, B):\n",
        "    if len(A) == len(B) and len(A[0]) == len(B[0]):\n",
        "        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]\n",
        "    return \"Error: Dimensiones incompatibles para suma.\"\n",
        "\n",
        "def multiplicar_matrices(A, B):\n",
        "    if len(A[0]) == len(B):\n",
        "        return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]\n",
        "    return \"Error: Columnas de A deben ser iguales a filas de B.\"\n",
        "\n",
        "def hadamard_matrices(A, B):\n",
        "    if len(A) == len(B) and len(A[0]) == len(B[0]):\n",
        "        return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]\n",
        "    return \"Error: Dimensiones incompatibles para Hadamard.\"\n",
        "\n",
        "def kronecker(A, B):\n",
        "    fA, cA = len(A), len(A[0])\n",
        "    fB, cB = len(B), len(B[0])\n",
        "    return [[A[i // fB][j // cB] * B[i % fB][j % cB] for j in range(cA * cB)] for i in range(fA * fB)]"
      ]
    }
  ]
}