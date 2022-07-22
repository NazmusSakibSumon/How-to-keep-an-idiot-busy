{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "38e64796",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing module\n",
    "import pyinputplus as pyip\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1c2e9f65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Do you want to keep an idiot busy for hours?\n",
      "yes\n",
      "Yeah. Lets go baby.\n"
     ]
    }
   ],
   "source": [
    "#Getting response\n",
    "prompt = 'Do you want to keep an idiot busy for hours?\\n'\n",
    "while True:\n",
    "    response = pyip.inputYesNo(prompt)\n",
    "    if response =='no':\n",
    "        print('Thank you. Have a nice day.')\n",
    "        sys.exit()\n",
    "    elif response == 'yes':\n",
    "        print('Yeah. Lets go baby.')\n",
    "        break\n",
    "    \n",
    "       \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "94a41f15",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Now we will create multiplication quizes to keep the idiot busy.\n",
    "#For that purpose, I need to import two more modules\n",
    "import random, time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b7d83609",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Creating variables to keep track of questions and answers\n",
    "numberOfQuestions = 10\n",
    "crrectAnswers = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1d4e1fd9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#0: 1 x 8 = 8\n",
      "Correct!\n",
      "#1: 0 x 1 = 0\n",
      "Correct!\n",
      "#2: 8 x 9 = 63\n",
      "Incorrect!\n",
      "#2: 8 x 9 = 63\n",
      "Incorrect!\n",
      "#2: 8 x 9 = 72\n",
      "Out of time!\n",
      "#3: 5 x 4 = 20\n",
      "Correct!\n",
      "#4: 7 x 8 = 56\n",
      "Correct!\n"
     ]
    }
   ],
   "source": [
    "# Now we will create a for loop for the program to pick two single-digit numbers to multiply. \n",
    "# The numbers will be picked randomly\n",
    "for questionNumber in range(numberOfQuestions):\n",
    "    num1 = random.randint(0,9)\n",
    "    num2 = random.randint(0,9)\n",
    "    \n",
    "    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)\n",
    "    try:\n",
    "        #Right answers are handles by allowRegexes\n",
    "        #Wrong answers are handles by blockRegexes, with a custom message.\n",
    "        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1 * num2)],\n",
    "                     blockRegexes = [('.*','Incorrect!')],\n",
    "                     timeout=8, limit=3)\n",
    "    except pyip.TimeoutException:\n",
    "        print('Out of time!')\n",
    "    except pyip.RetryLimitException:\n",
    "        print('Out of tries')\n",
    "    else:\n",
    "        #This block runs if no exceptions were raised in the try block\n",
    "        print('Correct!')\n",
    "        crrectAnswers+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8dcf6362",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Score: 4 / 5\n"
     ]
    }
   ],
   "source": [
    "#Let's place a 5 second pause at the end of the for loop to give the user time to read it.\n",
    "time.sleep(5)\n",
    "print('Score: %s / %s' % (crrectAnswers, numberOfQuestions))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1586ef5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Congratulations!! You passed the test\n"
     ]
    }
   ],
   "source": [
    "if (crrectAnswers/numberOfQuestions)*100 >=80:\n",
    "    print('Congratulations!! You passed the test.')\n",
    "else:\n",
    "    print('You failed the test you dumbass.')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
