{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOyb+BQMCxjGDRcgsJcHSQz",
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
        "<a href=\"https://colab.research.google.com/github/juanfelipegonzalezalfonso/tarea-programacion-arreglada-/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JnBhE0UEhKfl",
        "outputId": "125a0d79-ba75-4f4a-b41f-11d2b7913951",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- MENU DE OPERACIONES CON MATRICES ---\n",
            "1. Suma de matrices\n",
            "2. Multiplicación de matrices\n",
            "3. Producto de Hadamard\n",
            "4. Producto de Kronecker\n",
            "5. Salir\n"
          ]
        }
      ],
      "source": [
        "import menu\n",
        "import entrada\n",
        "import operaciones as ops\n",
        "\n",
        "\n",
        "while True:\n",
        "        opcion = menu.mostrar_menu()\n",
        "\n",
        "        if opcion == 5:\n",
        "            print(\"Saliendo del programa...\")\n",
        "            break\n",
        "\n",
        "        print(\"--- Matriz A ---\")\n",
        "        A = entrada.ingresar_matriz()\n",
        "        print(\"--- Matriz B ---\")\n",
        "        B = entrada.ingresar_matriz()\n",
        "\n",
        "        resultado = None\n",
        "        if opcion == 1:\n",
        "            resultado = ops.sumar_matrices(A, B)\n",
        "        elif opcion == 2:\n",
        "            resultado = ops.multiplicar_matrices(A, B)\n",
        "        elif opcion == 3:\n",
        "            resultado = ops.hadamard_matrices(A, B)\n",
        "        elif opcion == 4:\n",
        "            resultado = ops.kronecker(A, B)\n",
        "\n",
        "        if isinstance(resultado, str):\n",
        "            print(resultado)\n",
        "        else:\n",
        "            print(\"--- Resultado ---\")\n",
        "            entrada.mostrar_matriz(resultado)\n",
        "\n"
      ]
    }
  ]
}