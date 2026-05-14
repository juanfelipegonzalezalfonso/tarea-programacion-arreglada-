{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNgLfUDr3Vm7F2QFC+icjc/",
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
        "outputId": "0486b506-3a3a-4f8b-d665-6a72851b8494",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'menu'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_14637/4161097939.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mmenu\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mentrada\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0moperaciones_matrices\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mops\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mejecutar\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'menu'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import menu\n",
        "import entrada\n",
        "import operaciones_matrices as ops\n",
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
        "\n",
        "\n",
        ""
      ]
    }
  ]
}