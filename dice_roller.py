{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You rolled a die\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    print('You rolled a die')\n",
    "if __name__== \"__main__\":\n",
    "  main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You rolled a 3\n",
      "You have rolled a total of 3\n",
      "You rolled a 3\n",
      "You have rolled a total of 6\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "dice_rolls = 2\n",
    "dice_sum=0\n",
    "for i in range(0,dice_rolls):\n",
    "  roll = random.randint(1,6)\n",
    "  dice_sum= dice_sum + roll\n",
    "  print(f'You rolled a {roll}')\n",
    "  print(f'You have rolled a total of {dice_sum}') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
