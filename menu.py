{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMZbpT0E6ow6yPu5v0YQaJz",
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
        "<a href=\"https://colab.research.google.com/github/juanfelipegonzalezalfonso/tarea-programacion-arreglada-/blob/menu/menu.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ze0U5BzD6MgN",
        "outputId": "2bddf5db-9e8f-4f7b-ff39-af0267dcb6fc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing menu.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile menu.py\n",
        "def mostrar_menu():\n",
        "    print(\"\\n--- MENU DE OPERACIONES CON MATRICES ---\")\n",
        "    print(\"1. Suma de matrices\")\n",
        "    print(\"2. Multiplicación de matrices\")\n",
        "    print(\"3. Producto de Hadamard\")\n",
        "    print(\"4. Producto de Kronecker\")\n",
        "    print(\"5. Salir\")\n",
        "\n",
        "    while True:\n",
        "        try:\n",
        "            opcion = int(input(\"Seleccione una opción: \"))\n",
        "            if 1 <= opcion <= 5:\n",
        "                return opcion\n",
        "            print(\"Error: opción no válida.\")\n",
        "        except ValueError:\n",
        "            print(\"Error: debe ingresar un número entero.\")"
      ]
    }
  ]
}