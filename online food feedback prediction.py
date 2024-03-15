{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "df13ff32-a892-4cfc-823b-336d60271ce4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1df89266-cfc9-4a68-959f-df97a382ed5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"onlinefoods.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0ac5bf5e-d586-4394-b324-16b7d9fa43c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Marital Status</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Monthly Income</th>\n",
       "      <th>Educational Qualifications</th>\n",
       "      <th>Family size</th>\n",
       "      <th>latitude</th>\n",
       "      <th>longitude</th>\n",
       "      <th>Pin code</th>\n",
       "      <th>Output</th>\n",
       "      <th>Feedback</th>\n",
       "      <th>Unnamed: 12</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>No Income</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>4</td>\n",
       "      <td>12.9766</td>\n",
       "      <td>77.5993</td>\n",
       "      <td>560001</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>24</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>Below Rs.10000</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>3</td>\n",
       "      <td>12.9770</td>\n",
       "      <td>77.5773</td>\n",
       "      <td>560009</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>22</td>\n",
       "      <td>Male</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>Below Rs.10000</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>3</td>\n",
       "      <td>12.9551</td>\n",
       "      <td>77.6593</td>\n",
       "      <td>560017</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>22</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>No Income</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>6</td>\n",
       "      <td>12.9473</td>\n",
       "      <td>77.5616</td>\n",
       "      <td>560019</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>22</td>\n",
       "      <td>Male</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>Below Rs.10000</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>4</td>\n",
       "      <td>12.9850</td>\n",
       "      <td>77.5533</td>\n",
       "      <td>560010</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>383</th>\n",
       "      <td>23</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>No Income</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>2</td>\n",
       "      <td>12.9766</td>\n",
       "      <td>77.5993</td>\n",
       "      <td>560001</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>384</th>\n",
       "      <td>23</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>No Income</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>4</td>\n",
       "      <td>12.9854</td>\n",
       "      <td>77.7081</td>\n",
       "      <td>560048</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>385</th>\n",
       "      <td>22</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>No Income</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>5</td>\n",
       "      <td>12.9850</td>\n",
       "      <td>77.5533</td>\n",
       "      <td>560010</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>386</th>\n",
       "      <td>23</td>\n",
       "      <td>Male</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>Below Rs.10000</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>2</td>\n",
       "      <td>12.9770</td>\n",
       "      <td>77.5773</td>\n",
       "      <td>560009</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>387</th>\n",
       "      <td>23</td>\n",
       "      <td>Male</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>No Income</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>5</td>\n",
       "      <td>12.8988</td>\n",
       "      <td>77.5764</td>\n",
       "      <td>560078</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>388 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Age  Gender Marital Status Occupation  Monthly Income  \\\n",
       "0     20  Female         Single    Student       No Income   \n",
       "1     24  Female         Single    Student  Below Rs.10000   \n",
       "2     22    Male         Single    Student  Below Rs.10000   \n",
       "3     22  Female         Single    Student       No Income   \n",
       "4     22    Male         Single    Student  Below Rs.10000   \n",
       "..   ...     ...            ...        ...             ...   \n",
       "383   23  Female         Single    Student       No Income   \n",
       "384   23  Female         Single    Student       No Income   \n",
       "385   22  Female         Single    Student       No Income   \n",
       "386   23    Male         Single    Student  Below Rs.10000   \n",
       "387   23    Male         Single    Student       No Income   \n",
       "\n",
       "    Educational Qualifications  Family size  latitude  longitude  Pin code  \\\n",
       "0                Post Graduate            4   12.9766    77.5993    560001   \n",
       "1                     Graduate            3   12.9770    77.5773    560009   \n",
       "2                Post Graduate            3   12.9551    77.6593    560017   \n",
       "3                     Graduate            6   12.9473    77.5616    560019   \n",
       "4                Post Graduate            4   12.9850    77.5533    560010   \n",
       "..                         ...          ...       ...        ...       ...   \n",
       "383              Post Graduate            2   12.9766    77.5993    560001   \n",
       "384              Post Graduate            4   12.9854    77.7081    560048   \n",
       "385              Post Graduate            5   12.9850    77.5533    560010   \n",
       "386              Post Graduate            2   12.9770    77.5773    560009   \n",
       "387              Post Graduate            5   12.8988    77.5764    560078   \n",
       "\n",
       "    Output   Feedback Unnamed: 12  \n",
       "0      Yes   Positive         Yes  \n",
       "1      Yes   Positive         Yes  \n",
       "2      Yes  Negative          Yes  \n",
       "3      Yes   Positive         Yes  \n",
       "4      Yes   Positive         Yes  \n",
       "..     ...        ...         ...  \n",
       "383    Yes   Positive         Yes  \n",
       "384    Yes   Positive         Yes  \n",
       "385    Yes   Positive         Yes  \n",
       "386    Yes   Positive         Yes  \n",
       "387    Yes   Positive         Yes  \n",
       "\n",
       "[388 rows x 13 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bcbbc31c-ff10-4a08-b0cf-f0c501adb862",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Marital Status</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Monthly Income</th>\n",
       "      <th>Educational Qualifications</th>\n",
       "      <th>Family size</th>\n",
       "      <th>latitude</th>\n",
       "      <th>longitude</th>\n",
       "      <th>Pin code</th>\n",
       "      <th>Output</th>\n",
       "      <th>Feedback</th>\n",
       "      <th>Unnamed: 12</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>No Income</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>4</td>\n",
       "      <td>12.9766</td>\n",
       "      <td>77.5993</td>\n",
       "      <td>560001</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>24</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>Below Rs.10000</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>3</td>\n",
       "      <td>12.9770</td>\n",
       "      <td>77.5773</td>\n",
       "      <td>560009</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>22</td>\n",
       "      <td>Male</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>Below Rs.10000</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>3</td>\n",
       "      <td>12.9551</td>\n",
       "      <td>77.6593</td>\n",
       "      <td>560017</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>22</td>\n",
       "      <td>Female</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>No Income</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>6</td>\n",
       "      <td>12.9473</td>\n",
       "      <td>77.5616</td>\n",
       "      <td>560019</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>22</td>\n",
       "      <td>Male</td>\n",
       "      <td>Single</td>\n",
       "      <td>Student</td>\n",
       "      <td>Below Rs.10000</td>\n",
       "      <td>Post Graduate</td>\n",
       "      <td>4</td>\n",
       "      <td>12.9850</td>\n",
       "      <td>77.5533</td>\n",
       "      <td>560010</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age  Gender Marital Status Occupation  Monthly Income  \\\n",
       "0   20  Female         Single    Student       No Income   \n",
       "1   24  Female         Single    Student  Below Rs.10000   \n",
       "2   22    Male         Single    Student  Below Rs.10000   \n",
       "3   22  Female         Single    Student       No Income   \n",
       "4   22    Male         Single    Student  Below Rs.10000   \n",
       "\n",
       "  Educational Qualifications  Family size  latitude  longitude  Pin code  \\\n",
       "0              Post Graduate            4   12.9766    77.5993    560001   \n",
       "1                   Graduate            3   12.9770    77.5773    560009   \n",
       "2              Post Graduate            3   12.9551    77.6593    560017   \n",
       "3                   Graduate            6   12.9473    77.5616    560019   \n",
       "4              Post Graduate            4   12.9850    77.5533    560010   \n",
       "\n",
       "  Output   Feedback Unnamed: 12  \n",
       "0    Yes   Positive         Yes  \n",
       "1    Yes   Positive         Yes  \n",
       "2    Yes  Negative          Yes  \n",
       "3    Yes   Positive         Yes  \n",
       "4    Yes   Positive         Yes  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a86ac966-0419-42c5-afdd-0a22471416b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 388 entries, 0 to 387\n",
      "Data columns (total 13 columns):\n",
      " #   Column                      Non-Null Count  Dtype  \n",
      "---  ------                      --------------  -----  \n",
      " 0   Age                         388 non-null    int64  \n",
      " 1   Gender                      388 non-null    object \n",
      " 2   Marital Status              388 non-null    object \n",
      " 3   Occupation                  388 non-null    object \n",
      " 4   Monthly Income              388 non-null    object \n",
      " 5   Educational Qualifications  388 non-null    object \n",
      " 6   Family size                 388 non-null    int64  \n",
      " 7   latitude                    388 non-null    float64\n",
      " 8   longitude                   388 non-null    float64\n",
      " 9   Pin code                    388 non-null    int64  \n",
      " 10  Output                      388 non-null    object \n",
      " 11  Feedback                    388 non-null    object \n",
      " 12  Unnamed: 12                 388 non-null    object \n",
      "dtypes: float64(2), int64(3), object(8)\n",
      "memory usage: 39.5+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d946e34d-f4e5-4a23-bfe9-37c3087a3dab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age                           0\n",
       "Gender                        0\n",
       "Marital Status                0\n",
       "Occupation                    0\n",
       "Monthly Income                0\n",
       "Educational Qualifications    0\n",
       "Family size                   0\n",
       "latitude                      0\n",
       "longitude                     0\n",
       "Pin code                      0\n",
       "Output                        0\n",
       "Feedback                      0\n",
       "Unnamed: 12                   0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "393e14a1-aca6-4fff-8f35-2b716d7eb4c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=df, x='Gender')\n",
    "plt.title('Distribution of Gender')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7a6704ae-18c8-4ca0-97bf-cd0a67b9d3a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjsAAAHHCAYAAABZbpmkAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/H5lhTAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA/1klEQVR4nO3deXhN19/+8fskZJJJIoMQMc/z2JQaQ4xFVU1Vs8fU1tBWdTCXVluUarX6EFVqpq2WmmkVxfeL1kyNJSgiopUE6/dHfzmPIwmRhKS779d1nUv22uus/dnJdnJn77XPsRljjAAAACzKKasLAAAAeJgIOwAAwNIIOwAAwNIIOwAAwNIIOwAAwNIIOwAAwNIIOwAAwNIIOwAAwNIIOwAAwNIIO0AGjBw5Ujab7ZFsq27duqpbt659eePGjbLZbFq8ePEj2X7Xrl1VsGDBR7Kt9IqLi1PPnj0VHBwsm82mgQMHZnVJKXoYx03S8bBx48ZMHRewAsIO8P9FRUXJZrPZH25ubgoJCVFkZKSmTJmia9euZcp2zp49q5EjR2r37t2ZMl5mys61pcW4ceMUFRWlvn37as6cOercuXOqfQsWLCibzaaIiIgU18+YMcN+LOzcufNhlWw3btw4LV++/KFvR5J++eUXPf300woLC5Obm5vy5cunhg0baurUqZla0/79+zVy5EidOHEiYwUDGWUAGGOMmTVrlpFkRo8ebebMmWNmzpxpxo0bZxo1amRsNpsJCwsze/bscXhOYmKi+euvvx5oOzt27DCSzKxZsx7oefHx8SY+Pt6+vGHDBiPJLFq06IHGSW9tCQkJ5saNG5m2rYehRo0apmbNmmnqGxYWZtzc3IyTk5M5d+5csvV16tQxbm5uRpLZsWNHptaZ0nGTK1cu06VLl3SPmXQ8bNiw4Z79tmzZYlxcXEzRokXNmDFjzIwZM8zw4cNNo0aNTJEiRTK1pkWLFqWpJuBhy5GFOQvIlpo0aaKqVaval4cNG6b169erefPmevLJJ3XgwAG5u7tLknLkyKEcOR7uf6M///xTHh4ecnFxeajbuZ+cOXNm6fbT4sKFCypdunSa+9esWVM7duzQggUL9OKLL9rbz5w5ox9++EGtW7fWkiVLMq2+69evK1euXI/kuEnNW2+9JR8fH+3YsUO+vr4O6y5cuJAlNQEPG5exgDSoX7++3nzzTZ08eVJffPGFvT2luRdr1qxRrVq15OvrK09PT5UoUUKvvfaapL/nVVSrVk2S1K1bN/tlkqioKEl/z8spW7asdu3apdq1a8vDw8P+3Lvn7CS5deuWXnvtNQUHBytXrlx68skndfr0aYc+BQsWVNeuXZM9984x71dbSnN2rl+/riFDhig0NFSurq4qUaKE3nvvPRljHPrZbDYNGDBAy5cvV9myZeXq6qoyZcpo1apVKX/D73LhwgX16NFDQUFBcnNzU4UKFTR79mz7+qT5KsePH9e3335rr/1+l0/c3Nz01FNPad68eQ7tX375pXLnzq3IyMhkz9m7d6+6du2qwoULy83NTcHBwerevbsuXbrk0C/p2Ni/f786duyo3Llzq1atWg7r7vz+XL9+XbNnz7bXnvTzOnnypPr166cSJUrI3d1d/v7+atu2bbovDR07dkxlypRJFnQkKTAwMNNqioqKUtu2bSVJ9erVs4+RNKfIZrNp5MiRyWq4+1hNTEzUqFGjVKxYMbm5ucnf31+1atXSmjVr0rX/+HfizA6QRp07d9Zrr72m1atXq1evXin22bdvn5o3b67y5ctr9OjRcnV11dGjR7VlyxZJUqlSpTR69GgNHz5cvXv31hNPPCFJevzxx+1jXLp0SU2aNFH79u317LPPKigo6J51vfXWW7LZbBo6dKguXLigyZMnKyIiQrt377afgUqLtNR2J2OMnnzySW3YsEE9evRQxYoV9f333+vll1/W77//rkmTJjn0//HHH7V06VL169dPXl5emjJlitq0aaNTp07J398/1br++usv1a1bV0ePHtWAAQNUqFAhLVq0SF27dlVMTIxefPFFlSpVSnPmzNGgQYOUP39+DRkyRJIUEBBw3/3u2LGjGjVqpGPHjqlIkSKSpHnz5unpp59O8WzWmjVr9Ntvv6lbt24KDg7Wvn379Omnn2rfvn3atm1bsvDbtm1bFStWTOPGjUsWApPMmTNHPXv2VPXq1dW7d29JsteyY8cO/fTTT2rfvr3y58+vEydO6OOPP1bdunW1f/9+eXh43Hcf7xQWFqatW7fq119/VdmyZVPtl9GaateurRdeeEFTpkzRa6+9plKlSkmS/d+0GjlypMaPH2+vJTY2Vjt37tR//vMfNWzY8IHGwr9YFl9GA7KNpDk795qf4ePjYypVqmRfHjFihLnzv9GkSZOMJHPx4sVUx7jXvJg6deoYSWb69OkprqtTp459OWmORr58+UxsbKy9feHChUaS+eCDD+xtYWFhKc69uHvMe9XWpUsXExYWZl9evny5kWTGjh3r0O/pp582NpvNHD161N4mybi4uDi07dmzx0gyU6dOTbatO02ePNlIMl988YW9LSEhwYSHhxtPT0+HfQ8LCzPNmjW753h3971586YJDg42Y8aMMcYYs3//fiPJbNq0KcVj4s8//0w21pdffmkkmc2bN9vbko6NDh06JOt/93FjTOrzY1La3tatW40k8/nnn9vb0jpnZ/Xq1cbZ2dk4Ozub8PBw88orr5jvv//eJCQkJOub0ZruNWdHkhkxYkSy9ruP1QoVKqT5ZwqkhstYwAPw9PS8511ZSZcGvvrqK92+fTtd23B1dVW3bt3S3P+5556Tl5eXffnpp59W3rx59d1336Vr+2n13XffydnZWS+88IJD+5AhQ2SM0cqVKx3aIyIi7GcGJKl8+fLy9vbWb7/9dt/tBAcHq0OHDva2nDlz6oUXXlBcXJw2bdqUof1wdnbWM888oy+//FKSNHfuXIWGhtrPbN3tzrNlN27c0B9//KHHHntMkvSf//wnWf8+ffpkqL47t5eYmKhLly6paNGi8vX1TXF799OwYUNt3bpVTz75pPbs2aMJEyYoMjJS+fLl09dff50lNd2Lr6+v9u3bpyNHjmTquPh3IewADyAuLs4hWNytXbt2qlmzpnr27KmgoCC1b99eCxcufKDgky9fvgeajFysWDGHZZvNpqJFiz70231PnjypkJCQZN+PpMsUJ0+edGgvUKBAsjFy586tK1eu3Hc7xYoVk5OT48tVattJj44dO2r//v3as2eP5s2bp/bt26f6PjiXL1/Wiy++qKCgILm7uysgIECFChWSJF29ejVZ/6R16fXXX39p+PDh9nlRefLkUUBAgGJiYlLcXlpUq1ZNS5cu1ZUrV/Tzzz9r2LBhunbtmp5++mnt378/S2pKzejRoxUTE6PixYurXLlyevnll7V3795M3Qasj7ADpNGZM2d09epVFS1aNNU+7u7u2rx5s9auXavOnTtr7969ateunRo2bKhbt26laTsPMs8mrVL7xZ3WmjKDs7Nziu0mlXksj1KNGjVUpEgRDRw4UMePH1fHjh1T7fvMM89oxowZ6tOnj5YuXarVq1fbJ1qnFGoz+vN8/vnn9dZbb+mZZ57RwoULtXr1aq1Zs0b+/v7pPnuYxMXFRdWqVdO4ceP08ccfKzExUYsWLcrSmu4+JmvXrq1jx45p5syZKlu2rD777DNVrlxZn332WYa2g38XJigDaTRnzhxJSvEOnTs5OTmpQYMGatCggSZOnKhx48bp9ddf14YNGxQREZHp75x79+l9Y4yOHj2q8uXL29ty586tmJiYZM89efKkChcubF9+kNrCwsK0du1aXbt2zeHszsGDB+3rM0NYWJj27t2r27dvO5zdyeztdOjQQWPHjlWpUqVUsWLFFPtcuXJF69at06hRozR8+HB7e2ZcYknte7948WJ16dJF77//vr3txo0bKf48MyLp7RbOnTuXaTXd63hK6ZhMSEhw2H4SPz8/devWTd26dVNcXJxq166tkSNHqmfPnvfbLUASZ3aANFm/fr3GjBmjQoUKqVOnTqn2u3z5crK2pF+c8fHxkqRcuXJJUqb9svr8888d5hEtXrxY586dU5MmTextRYoU0bZt25SQkGBvW7FiRbJb1B+ktqZNm+rWrVv68MMPHdonTZokm83msP2MaNq0qaKjo7VgwQJ7282bNzV16lR5enqqTp06mbKdnj17asSIEQ6/wO+WdHbq7rNRkydPzvD2c+XKleL33dnZOdn2pk6dmu6zchs2bEjxbFrSHK8SJUpkWk33Op6KFCmizZs3O7R9+umnyca4+5Z+T09PFS1a1P7/CUgLzuwAd1m5cqUOHjyomzdv6vz581q/fr3WrFmjsLAwff3113Jzc0v1uaNHj9bmzZvVrFkzhYWF6cKFC/roo4+UP39++3usFClSRL6+vpo+fbq8vLyUK1cu1ahRI91zO/z8/FSrVi1169ZN58+f1+TJk1W0aFGH2+N79uypxYsXq3HjxnrmmWd07NgxffHFFw4Thh+0thYtWqhevXp6/fXXdeLECVWoUEGrV6/WV199pYEDByYbO7169+6tTz75RF27dtWuXbtUsGBBLV68WFu2bNHkyZPvOYfqQYSFhaX4vi938vb2Vu3atTVhwgQlJiYqX758Wr16tY4fP57h7VepUkVr167VxIkTFRISokKFCqlGjRpq3ry55syZIx8fH5UuXVpbt27V2rVr73m7/r08//zz+vPPP9W6dWuVLFlSCQkJ+umnn7RgwQIVLFjQYXJ8RmuqWLGinJ2d9c477+jq1atydXVV/fr1FRgYqJ49e6pPnz5q06aNGjZsqD179uj7779Xnjx5HMYoXbq06tatqypVqsjPz087d+7U4sWLNWDAgHTtP/6lsvBOMCBbSbrNOOnh4uJigoODTcOGDc0HH3zgcItzkrtvIV63bp1p2bKlCQkJMS4uLiYkJMR06NDBHD582OF5X331lSldurTJkSOHw63ederUMWXKlEmxvtRuPf/yyy/NsGHDTGBgoHF3dzfNmjUzJ0+eTPb8999/3+TLl8+4urqamjVrmp07dyYb81613X3ruTHGXLt2zQwaNMiEhISYnDlzmmLFipl3333X3L5926GfJNO/f/9kNaV2S/zdzp8/b7p162by5MljXFxcTLly5VK8PT49t57fS0q3np85c8a0bt3a+Pr6Gh8fH9O2bVtz9uzZZLdSJx0bKb0NQUq3nh88eNDUrl3buLu7G0n278uVK1fs++7p6WkiIyPNwYMHk33v0nrr+cqVK0337t1NyZIljaenp/2jI55//nlz/vz5TK3JGGNmzJhhChcubJydnR3qu3Xrlhk6dKjJkyeP8fDwMJGRkebo0aPJxhg7dqypXr268fX1Ne7u7qZkyZLmrbfeSvFWeSA1NmOywexAAACAh4Q5OwAAwNIIOwAAwNIIOwAAwNIIOwAAwNIIOwAAwNIIOwAAwNJ4U0H9/Xk2Z8+elZeXV6a/lT8AAHg4jDG6du2aQkJCkn1Y8J0IO5LOnj2r0NDQrC4DAACkw+nTp5U/f/5U1xN2JPvbzZ8+fVre3t5ZXA0AAEiL2NhYhYaG3vdjYwg7+r9P5vX29ibsAADwD3O/KShMUAYAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJZG2AEAAJaWI6sLsIoqL3+e1SUgG9n17nNZXQIA4P/jzA4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALC0LA0748ePV7Vq1eTl5aXAwEC1atVKhw4dcuhTt25d2Ww2h0efPn0c+pw6dUrNmjWTh4eHAgMD9fLLL+vmzZuPclcAAEA2lSMrN75p0yb1799f1apV082bN/Xaa6+pUaNG2r9/v3LlymXv16tXL40ePdq+7OHhYf/61q1batasmYKDg/XTTz/p3Llzeu6555QzZ06NGzfuke4PAADIfrI07KxatcphOSoqSoGBgdq1a5dq165tb/fw8FBwcHCKY6xevVr79+/X2rVrFRQUpIoVK2rMmDEaOnSoRo4cKRcXl4e6DwAAIHvLVnN2rl69Kkny8/NzaJ87d67y5MmjsmXLatiwYfrzzz/t67Zu3apy5copKCjI3hYZGanY2Fjt27cvxe3Ex8crNjbW4QEAAKwpS8/s3On27dsaOHCgatasqbJly9rbO3bsqLCwMIWEhGjv3r0aOnSoDh06pKVLl0qSoqOjHYKOJPtydHR0itsaP368Ro0a9ZD2BAAAZCfZJuz0799fv/76q3788UeH9t69e9u/LleunPLmzasGDRro2LFjKlKkSLq2NWzYMA0ePNi+HBsbq9DQ0PQVDgAAsrVscRlrwIABWrFihTZs2KD8+fPfs2+NGjUkSUePHpUkBQcH6/z58w59kpZTm+fj6uoqb29vhwcAALCmLA07xhgNGDBAy5Yt0/r161WoUKH7Pmf37t2SpLx580qSwsPD9csvv+jChQv2PmvWrJG3t7dKly79UOoGAAD/HFl6Gat///6aN2+evvrqK3l5ednn2Pj4+Mjd3V3Hjh3TvHnz1LRpU/n7+2vv3r0aNGiQateurfLly0uSGjVqpNKlS6tz586aMGGCoqOj9cYbb6h///5ydXXNyt0DAADZQJae2fn444919epV1a1bV3nz5rU/FixYIElycXHR2rVr1ahRI5UsWVJDhgxRmzZt9M0339jHcHZ21ooVK+Ts7Kzw8HA9++yzeu655xzelwcAAPx7ZemZHWPMPdeHhoZq06ZN9x0nLCxM3333XWaVBQAALCRbTFAGAAB4WAg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0gg7AADA0rI07IwfP17VqlWTl5eXAgMD1apVKx06dMihz40bN9S/f3/5+/vL09NTbdq00fnz5x36nDp1Ss2aNZOHh4cCAwP18ssv6+bNm49yVwAAQDaVpWFn06ZN6t+/v7Zt26Y1a9YoMTFRjRo10vXr1+19Bg0apG+++UaLFi3Spk2bdPbsWT311FP29bdu3VKzZs2UkJCgn376SbNnz1ZUVJSGDx+eFbsEAACyGZsxxmR1EUkuXryowMBAbdq0SbVr19bVq1cVEBCgefPm6emnn5YkHTx4UKVKldLWrVv12GOPaeXKlWrevLnOnj2roKAgSdL06dM1dOhQXbx4US4uLvfdbmxsrHx8fHT16lV5e3unq/YqL3+erufBmna9+1xWlwAAlpfW39/Zas7O1atXJUl+fn6SpF27dikxMVERERH2PiVLllSBAgW0detWSdLWrVtVrlw5e9CRpMjISMXGxmrfvn0pbic+Pl6xsbEODwAAYE3ZJuzcvn1bAwcOVM2aNVW2bFlJUnR0tFxcXOTr6+vQNygoSNHR0fY+dwadpPVJ61Iyfvx4+fj42B+hoaGZvDcAACC7yDZhp3///vr11181f/78h76tYcOG6erVq/bH6dOnH/o2AQBA1siR1QVI0oABA7RixQpt3rxZ+fPnt7cHBwcrISFBMTExDmd3zp8/r+DgYHufn3/+2WG8pLu1kvrczdXVVa6urpm8FwAAIDvK0jM7xhgNGDBAy5Yt0/r161WoUCGH9VWqVFHOnDm1bt06e9uhQ4d06tQphYeHS5LCw8P1yy+/6MKFC/Y+a9askbe3t0qXLv1odgQAAGRbWXpmp3///po3b56++uoreXl52efY+Pj4yN3dXT4+PurRo4cGDx4sPz8/eXt76/nnn1d4eLgee+wxSVKjRo1UunRpde7cWRMmTFB0dLTeeOMN9e/fn7M3AAAga8POxx9/LEmqW7euQ/usWbPU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sNatW2dvi42N1fbt2xUeHi5JCg8PV0xMjHbt2mXvs379et2+fVs1atR45DUDAIDsJ0vvxoqLi9PRo0fty8ePH9fu3bvl5+enAgUKaODAgRo7dqyKFSumQoUK6c0331RISIhatWolSSpVqpQaN26sXr16afr06UpMTNSAAQPUvn177sQCAACSsjjs7Ny5U/Xq1bMvDx48WJLUpUsXRUVF6ZVXXtH169fVu3dvxcTEqFatWlq1apXc3Nzsz5k7d64GDBigBg0ayMnJSW3atNGUKVMe+b4AAIDsKUvDTt26dWWMSXW9zWbT6NGjNXr06FT7+Pn5ad68eQ+jPAAAYAHZds4OAABAZiDsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAASyPsAAAAS8vWYWfkyJGy2WwOj5IlS9rX37hxQ/3795e/v788PT3Vpk0bnT9/PgsrBgAA2U22DjuSVKZMGZ07d87++PHHH+3rBg0apG+++UaLFi3Spk2bdPbsWT311FNZWC0AAMhucmR1AfeTI0cOBQcHJ2u/evWq/vd//1fz5s1T/fr1JUmzZs1SqVKltG3bNj322GOPulQAAJANZfszO0eOHFFISIgKFy6sTp066dSpU5KkXbt2KTExUREREfa+JUuWVIECBbR169Z7jhkfH6/Y2FiHBwAAsKZsHXZq1KihqKgorVq1Sh9//LGOHz+uJ554QteuXVN0dLRcXFzk6+vr8JygoCBFR0ffc9zx48fLx8fH/ggNDX2IewEAALJStr6M1aRJE/vX5cuXV40aNRQWFqaFCxfK3d093eMOGzZM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Vo4cOexnjO5WqlQpbd++Xc8995y9bdu2bZlWAxzlypVLRYsWTXP/ypUra8GCBQoMDJS3t3eanvOoX3tKlSqlJUuWyBhj/yNxy5Yt8vLyUv78+SVJLi4uqZ6FuVNK/UqVKmV/y5AkW7ZsUfHixe/5h2Px4sVVvHhxDRo0SB06dNCsWbPUunVrbdmyRS1bttSzzz4r6e8/aA8fPqzSpUs7PL9nz56aPHmyfv/9d0VERCg0NPT+34xHjMtY/3KXLl1S/fr19cUXX2jv3r06fvy4Fi1apAkTJqhly5bpGvP555/Xd999p4kTJ+rIkSP65JNPtHLlynue1hw1apTGjx+vKVOm6PDhw/rll180a9YsTZw4Mb27hn8YZ2dnHThwQPv370/2wpw7d275+/vr008/1dGjR7V+/XoNHjw407YdERGh8PBwtWrVSqtXr9aJEyf0008/6fXXX7ffmfLiiy9q5syZmjVrlg4fPqwRI0Zo3759mVYDMqZTp07KkyePWrZsqR9++EHHjx/Xxo0b9cILL9zzEtGjfO3p16+fTp8+reeff14HDx7UV199pREjRmjw4MFycvr713HBggW1fft2nThxQn/88UeqZ4UKFiyozZs36/fff9cff/whSRoyZIjWrVunMWPG6PDhw5o9e7Y+/PBDvfTSSymO8ddff2nAgAHauHGjTp48qS1btmjHjh0qVaqUJKlYsWJas2aNfvrpJx04cED/8z//o/Pnzycbp2PHjjpz5oxmzJih7t27Z8a3KtMRdv7lPD09VaNGDU2aNEm1a9dW2bJl9eabb6pXr1768MMP0zVmzZo1NX36dE2cOFEVKlTQqlWrNGjQILm5uaX6nJ49e+qzzz7TrFmzVK5cOdWpU0dRUVEqVKhQencN/0De3t4p/lXu5OSk+fPna9euXSpbtqwGDRqkd999N9O2a7PZ9N1336l27drq1q2bihcvrvbt2+vkyZMKCgqSJLVr105vvvmmXnnlFVWpUkUnT55U3759M60GZIyHh4c2b96sAgUK6KmnnlKpUqXsbw9wrzM9j/K1J1++fPruu+/0888/q0KFCurTp4969OihN954w97npZdekrOzs0qXLq2AgIBkc9KSjB49WidOnFCRIkXsl+kqV66shQsXav78+SpbtqyGDx+u0aNHpzodwdnZWZcuXdJzzz2n4sWL65lnnlGTJk00atQoSdIbb7yhypUrKzIyUnXr1lVwcLBatWqVbBwfHx+1adNGnp6eKa7PDmzGGJPVRcD6evXqpYMHD+qHH37I6lIAAJmsQYMGKlOmjKZMmZLVpaSIOTt4KN577z01bNhQuXLl0sqVKzV79mzeJBAALObKlSvauHGjNm7cmK1f4wk7eCh+/vlnTZgwQdeuXVPhwoU1ZcoU9ezZM6vLAgBkokqVKunKlSt655137O9knR1xGQsAAFgaE5QBAIClEXYAAIClEXYAAIClEXYAAIClEXYAZBtRUVGZ8llUmTUOAGsg7AC4r6RPMe7Tp0+ydf3795fNZkv1XVofRLt27XT48GH78siRI1WxYsUMj5uSTZs2qX79+vLz85OHh4eKFSumLl262D/kML2BaePGjbLZbIqJicncggGkG2EHQJqEhoZq/vz5+uuvv+xtN27c0Lx581SgQIEMj5+YmCh3d3cFBgZmeKz72b9/vxo3bqyqVatq8+bN+uWXXzR16tQ0fwgjgH8Wwg6ANKlcubJCQ0O1dOlSe9vSpUtVoEABVapUyaHvqlWrVKtWLfn6+srf31/NmzfXsWPH7OtPnDghm82mBQsWqE6dOnJzc9PcuXMdzqZERUVp1KhR2rNnj2w2m2w2m6KioiRJEydOVLly5ZQrVy6FhoaqX79+iouLS/O+rF69WsHBwZowYYLKli2rIkWKqHHjxpoxY4bc3d21ceNGdevWTVevXrVve+TIkZKkOXPmqGrVqvLy8lJwcLA6duyoCxcu2PerXr16kv7+8NI7z3gVLFhQkydPdqijYsWK9nGNMRo5cqQKFCggV1dXhYSE6IUXXkjzPgFIHWEHQJp1795ds2bNsi/PnDlT3bp1S9bv+vXrGjx4sHbu3Kl169bJyclJrVu3TvYJzq+++qpefPFFHThwQJGRkQ7r2rVrpyFDhqhMmTI6d+6czp07p3bt2kn6+4NBp0yZon379mn27Nlav369XnnllTTvR3BwsM6dO6fNmzenuP7xxx/X5MmT5e3tbd920idHJyYmasyYMdqzZ4+WL1+uEydO2ANNaGiolixZIkk6dOiQzp07pw8++CBNNS1ZskSTJk3SJ598oiNHjmj58uUqV65cmvcJQOr4uAgAafbss89q2LBhOnnypCRpy5Ytmj9/vjZu3OjQr02bNg7LM2fOVEBAgPbv36+yZcva2wcOHKinnnoqxW25u7vL09NTOXLkUHBwsMO6gQMH2r8uWLCgxo4dqz59+qT5s3natm2r77//XnXq1FFwcLAee+wxNWjQQM8995y8vb3l4uIiHx8f2Wy2ZNvu3r27/eukj0KpVq2a4uLi5OnpKT8/P0lSYGDgA835OXXqlIKDgxUREaGcOXOqQIECql69epqfDyB1nNkBkGYBAQFq1qyZoqKiNGvWLDVr1kx58uRJ1u/IkSPq0KGDChcuLG9vbxUsWFDS37/Q71S1atV01bF27Vo1aNBA+fLlk5eXlzp37qxLly7pzz//TNPznZ2dNWvWLJ05c0YTJkxQvnz5NG7cOPtZpHvZtWuXWrRooQIFCsjLy0t16tRJcd8eVNu2bfXXX3+pcOHC6tWrl5YtW6abN29maEwAfyPsAHgg3bt3V1RUlGbPnu1wluNOLVq00OXLlzVjxgxt375d27dvlyT7nU5JcuXK9cDbP3HihJo3b67y5ctryZIl2rVrl6ZNm5bi+PeTL18+de7cWR9++KH27dunGzduaPr06an2v379uiIjI+Xt7a25c+dqx44dWrZsWZq27eTkpLs/ijAxMdH+dWhoqA4dOqSPPvpI7u7u6tevn2rXru3QB0D6cBkLwANp3LixEhISZLPZks2zkaRLly7p0KFDmjFjhp544glJ0o8//piubaV0d9SuXbt0+/Ztvf/++3Jy+vvvtYULF6Zr/Dvlzp1befPm1fXr11Pd9sGDB3Xp0iW9/fbbCg0NlSTt3LkzWc2Skj03ICDA4axRbGysjh8/7tDH3d1dLVq0UIsWLdS/f3+VLFlSv/zyiypXrpzh/QP+zQg7AB6Is7OzDhw4YP/6brlz55a/v78+/fRT5c2bV6dOndKrr76arm0VLFhQx48f1+7du5U/f355eXmpaNGiSkxM1NSpU9WiRQtt2bLlnmdjUvLJJ59o9+7dat26tYoUKaIbN27o888/1759+zR16lT7tuPi4rRu3TpVqFBBHh4eKlCggFxcXDR16lT16dNHv/76q8aMGeMwdlhYmGw2m1asWKGmTZva5x7Vr19fUVFRatGihXx9fTV8+HCH719UVJRu3bqlGjVqyMPDQ1988YXc3d0VFhaWru8dgP/DZSwAD8zb21ve3t4prnNyctL8+fO1a9culS1bVoMGDdK7776bru20adNGjRs3Vr169RQQEKAvv/xSFSpU0MSJE/XOO++obNmymjt3rsaPH/9A41avXl1xcXHq06ePypQpozp16mjbtm1avny5fQ7O448/rj59+qhdu3YKCAjQhAkTFBAQoKioKC1atEilS5fW22+/rffee89h7Hz58mnUqFF69dVXFRQUpAEDBkiShg0bpjp16qh58+Zq1qyZWrVqpSJFitif5+vrqxkzZqhmzZoqX7681q5dq2+++Ub+/v7p+t4B+D82c/dFZAAAAAvhzA4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALA0wg4AALC0/wdw4iR5uF7SQwAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=df, x='Marital Status')\n",
    "plt.title('Distribution of Marital Status')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "994de505-9916-4627-a4eb-170e964ac045",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjIAAAHHCAYAAACle7JuAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/H5lhTAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA4EklEQVR4nO3de1hVZd7/8c9WOSmC4gEkOVg64DEPY0pWmpLk2MFHGrOyPKbToKb2TEVZllPRTKU2hTk1imU5HnrSaCxN8VQNOkqZWh4nFScORgqIIoLcvz/mcv/aAoq4N3svfL+ua11X+15rf9f3jtp+XNxrbZsxxggAAMCC6rm7AQAAgJoiyAAAAMsiyAAAAMsiyAAAAMsiyAAAAMsiyAAAAMsiyAAAAMsiyAAAAMsiyAAAAMsiyAAW99xzz8lms9XKufr166d+/frZX2/cuFE2m00ffvhhrZx/1KhRioyMrJVz1VRRUZHGjRunkJAQ2Ww2TZkyxd0tAXUaQQbwIAsXLpTNZrNvvr6+Cg0NVVxcnP7yl7/o5MmTTjlPVlaWnnvuOe3YscMp9ZzJk3urjpdeekkLFy7UI488okWLFunBBx+85HvOnTun0NBQ2Ww2ffbZZ7XQJVB3NHB3AwAqmjlzptq0aaPS0lLl5ORo48aNmjJlimbNmqXU1FR16dLFfuz06dP15JNPXlb9rKwsPf/884qMjFTXrl2r/b7PP//8ss5TExfr7Z133lF5ebnLe7gS69evV+/evTVjxozLek92drYiIyP1wQcfaNCgQS7sEKhbCDKABxo0aJB+/etf218nJiZq/fr1uuOOO3TXXXdpz5498vPzkyQ1aNBADRq49n/l06dPq2HDhvL29nbpeS7Fy8vLreevjmPHjqlDhw6X9Z73339f3bt318iRI/XUU0/p1KlTatSokYs6BOoWfrUEWET//v31zDPP6MiRI3r//fft45WtkVm7dq1uuukmNWnSRP7+/oqKitJTTz0l6b/rWnr27ClJGj16tP3XWAsXLpT033UwnTp1UkZGhm655RY1bNjQ/t4L18icd+7cOT311FMKCQlRo0aNdNddd+no0aMOx0RGRmrUqFEV3vvLmpfqrbI1MqdOndJjjz2msLAw+fj4KCoqSq+++qqMMQ7H2Ww2TZw4UStXrlSnTp3k4+Ojjh07avXq1ZX/C7/AsWPHNHbsWAUHB8vX11fXX3+93n33Xfv+8+uFDh06pFWrVtl7P3z48EXrFhcXa8WKFRo+fLiGDRum4uJiffzxx5Ueu3z5cnXo0EG+vr7q1KmTVqxYUem/k/Lycs2ZM0cdO3aUr6+vgoODNWHCBJ04caJacwWshCADWMj59RYX+xXPd999pzvuuEMlJSWaOXOmXnvtNd1111366quvJEnt27fXzJkzJUnjx4/XokWLtGjRIt1yyy32Gj///LMGDRqkrl27as6cObr11lsv2teLL76oVatW6YknntDkyZO1du1axcbGqri4+LLmV53efskYo7vuukuzZ8/W7bffrlmzZikqKkp/+MMfNG3atArHf/nll/r973+v4cOH689//rPOnDmj+Ph4/fzzzxftq7i4WP369dOiRYv0wAMP6JVXXlFgYKBGjRql119/3d77okWL1Lx5c3Xt2tXee4sWLS5aOzU1VUVFRRo+fLhCQkLUr18/ffDBBxWOW7Vqle699155eXkpKSlJQ4cO1dixY5WRkVHh2AkTJugPf/iD+vTpo9dff12jR4/WBx98oLi4OJWWll60H8ByDACPkZKSYiSZbdu2VXlMYGCg6datm/31jBkzzC//V549e7aRZH766acqa2zbts1IMikpKRX29e3b10gy8+bNq3Rf37597a83bNhgJJlrrrnGFBYW2seXLVtmJJnXX3/dPhYREWFGjhx5yZoX623kyJEmIiLC/nrlypVGknnhhRccjrvnnnuMzWYzBw8etI9JMt7e3g5j3377rZFk3njjjQrn+qU5c+YYSeb999+3j509e9bExMQYf39/h7lHRESYwYMHX7TeL91xxx2mT58+9tdvv/22adCggTl27JjDcZ07dzatW7c2J0+etI9t3LjRSHL4d/LFF18YSeaDDz5weP/q1asrHQesjisygMX4+/tf9O6lJk2aSJI+/vjjGi+M9fHx0ejRo6t9/EMPPaTGjRvbX99zzz1q1aqVPv300xqdv7o+/fRT1a9fX5MnT3YYf+yxx2SMqXAHUGxsrK677jr76y5duiggIEA//PDDJc8TEhKi++67zz7m5eWlyZMnq6ioSJs2bapR/z///LPWrFnjUDc+Pl42m03Lli2zj2VlZWnXrl166KGH5O/vbx/v27evOnfu7FBz+fLlCgwM1G233aa8vDz71qNHD/n7+2vDhg016hXwVAQZwGKKioocQsOF7r33XvXp00fjxo1TcHCwhg8frmXLll1WqLnmmmsua2Fvu3btHF7bbDa1bdv2kutDrtSRI0cUGhpa4d9H+/bt7ft/KTw8vEKNpk2bXnLtyJEjR9SuXTvVq+f4kVnVeapr6dKlKi0tVbdu3XTw4EEdPHhQx48fV69evRx+vXS+ftu2bSvUuHDswIEDKigoUMuWLdWiRQuHraioSMeOHatRr4Cn4q4lwEL+85//qKCgoNI/0M7z8/PT5s2btWHDBq1atUqrV6/W0qVL1b9/f33++eeqX7/+Jc9z/o4oZ6rqoX3nzp2rVk/OUNV5zAULg2vL+bDSp0+fSvf/8MMPuvbaay+rZnl5uVq2bFnpOhtJl1yzA1gNQQawkEWLFkmS4uLiLnpcvXr1NGDAAA0YMECzZs3SSy+9pKefflobNmxQbGys058EfODAAYfXxhgdPHjQ4Xk3TZs2VX5+foX3HjlyxOEP68vpLSIiQuvWrdPJkycdrsrs3bvXvt8ZIiIitHPnTpWXlztclbmS8xw6dEj//Oc/NXHiRPXt29dhX3l5uR588EEtXrxY06dPt9c/ePBghToXjl133XVat26d+vTp45JACngafrUEWMT69ev1xz/+UW3atNEDDzxQ5XHHjx+vMHb+wXIlJSWSZH9GSWXBoibee+89h3U7H374obKzsx0e7Hbddddpy5YtOnv2rH3sH//4R4XbtC+nt9/85jc6d+6c3nzzTYfx2bNny2azOe3Bcr/5zW+Uk5OjpUuX2sfKysr0xhtvyN/fv0IQqY7zV0wef/xx3XPPPQ7bsGHD1LdvX/sxoaGh6tSpk9577z0VFRXZa2zatEm7du1yqDts2DCdO3dOf/zjHyucs6yszGk/c8BTcEUG8ECfffaZ9u7dq7KyMuXm5mr9+vVau3atIiIilJqaKl9f3yrfO3PmTG3evFmDBw9WRESEjh07prlz56p169a66aabJP03VDRp0kTz5s1T48aN1ahRI/Xq1Utt2rSpUb9BQUG66aabNHr0aOXm5mrOnDlq27atHn74Yfsx48aN04cffqjbb79dw4YN07///W+9//77DotvL7e3O++8U7feequefvppHT58WNdff70+//xzffzxx5oyZUqF2jU1fvx4/fWvf9WoUaOUkZGhyMhIffjhh/rqq680Z86ci65ZqsoHH3ygrl27KiwsrNL9d911lyZNmqSvv/5a3bt310svvaS7775bffr00ejRo3XixAm9+eab6tSpk0O46du3ryZMmKCkpCTt2LFDAwcOlJeXlw4cOKDly5fr9ddf1z333FPjfxeAx3HzXVMAfuH87dfnN29vbxMSEmJuu+028/rrrzvc5nvehbdfp6WlmbvvvtuEhoYab29vExoaau677z6zf/9+h/d9/PHHpkOHDqZBgwYOtzv37dvXdOzYsdL+qrr9+u9//7tJTEw0LVu2NH5+fmbw4MHmyJEjFd7/2muvmWuuucb4+PiYPn36mO3bt1eoebHeLrz92hhjTp48aaZOnWpCQ0ONl5eXadeunXnllVdMeXm5w3GSTEJCQoWeqrot/EK5ublm9OjRpnnz5sbb29t07ty50lvEq3P7dUZGhpFknnnmmSqPOXz4sJFkpk6dah9bsmSJiY6ONj4+PqZTp04mNTXVxMfHm+jo6Arvf/vtt02PHj2Mn5+fady4sencubN5/PHHTVZW1iXnCliJzRg3rXIDAFyxrl27qkWLFlq7dq27WwHcgjUyAGABpaWlKisrcxjbuHGjvv3220q/NgK4WnBFBgAs4PDhw4qNjdWIESMUGhqqvXv3at68eQoMDNTu3bvVrFkzd7cIuAWLfQHAApo2baoePXrob3/7m3766Sc1atRIgwcP1ssvv0yIwVWNKzIAAMCyWCMDAAAsiyADAAAsq86vkSkvL1dWVpYaN27s9MeyAwAA1zDG6OTJkwoNDa3wha2/VOeDTFZWVpVPzgQAAJ7t6NGjat26dZX763yQOf/o8KNHjyogIMDN3QAAgOooLCxUWFjYJb8CpM4HmfO/TgoICCDIAABgMZdaFsJiXwAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkN3N0AcDXKzMxUXl6ey+o3b95c4eHhLqsPAJ6CIAPUsszMTEVHt1dx8WmXncPPr6H27t1DmAFQ5xFkgFqWl5en4uLT6jVmhgJaRTq9fmH2YW1d8Lzy8vIIMgDqPIIM4CYBrSIVFB7l7jYAwNJY7AsAACyLIAMAACyLIAMAACyLIAMAACyLIAMAACyLIAMAACyLIAMAACzLrUEmMjJSNputwpaQkCBJOnPmjBISEtSsWTP5+/srPj5eubm57mwZAAB4ELcGmW3btik7O9u+rV27VpL029/+VpI0depUffLJJ1q+fLk2bdqkrKwsDR061J0tAwAAD+LWJ/u2aNHC4fXLL7+s6667Tn379lVBQYHmz5+vxYsXq3///pKklJQUtW/fXlu2bFHv3r3d0TIAAPAgHrNG5uzZs3r//fc1ZswY2Ww2ZWRkqLS0VLGxsfZjoqOjFR4ervT09CrrlJSUqLCw0GEDAAB1k8cEmZUrVyo/P1+jRo2SJOXk5Mjb21tNmjRxOC44OFg5OTlV1klKSlJgYKB9CwsLc2HXAADAnTwmyMyfP1+DBg1SaGjoFdVJTExUQUGBfTt69KiTOgQAAJ7GI779+siRI1q3bp0++ugj+1hISIjOnj2r/Px8h6syubm5CgkJqbKWj4+PfHx8XNkuAADwEB5xRSYlJUUtW7bU4MGD7WM9evSQl5eX0tLS7GP79u1TZmamYmJi3NEmAADwMG6/IlNeXq6UlBSNHDlSDRr8/3YCAwM1duxYTZs2TUFBQQoICNCkSZMUExPDHUsAAECSBwSZdevWKTMzU2PGjKmwb/bs2apXr57i4+NVUlKiuLg4zZ071w1dAgAAT+T2IDNw4EAZYyrd5+vrq+TkZCUnJ9dyVwAAwAo8Yo0MAABATRBkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZbk9yPz4448aMWKEmjVrJj8/P3Xu3Fnbt2+37zfG6Nlnn1WrVq3k5+en2NhYHThwwI0dAwAAT+HWIHPixAn16dNHXl5e+uyzz/T999/rtddeU9OmTe3H/PnPf9Zf/vIXzZs3T1u3blWjRo0UFxenM2fOuLFzAADgCRq48+R/+tOfFBYWppSUFPtYmzZt7P9sjNGcOXM0ffp03X333ZKk9957T8HBwVq5cqWGDx9e6z0DAADP4dYrMqmpqfr1r3+t3/72t2rZsqW6deumd955x77/0KFDysnJUWxsrH0sMDBQvXr1Unp6eqU1S0pKVFhY6LABAIC6ya1B5ocfftBbb72ldu3aac2aNXrkkUc0efJkvfvuu5KknJwcSVJwcLDD+4KDg+37LpSUlKTAwED7FhYW5tpJAAAAt3FrkCkvL1f37t310ksvqVu3bho/frwefvhhzZs3r8Y1ExMTVVBQYN+OHj3qxI4BAIAncWuQadWqlTp06OAw1r59e2VmZkqSQkJCJEm5ubkOx+Tm5tr3XcjHx0cBAQEOGwAAqJvcGmT69Omjffv2OYzt379fERERkv678DckJERpaWn2/YWFhdq6datiYmJqtVcAAOB53HrX0tSpU3XjjTfqpZde0rBhw/Svf/1Lb7/9tt5++21Jks1m05QpU/TCCy+oXbt2atOmjZ555hmFhoZqyJAh7mwdAAB4ALcGmZ49e2rFihVKTEzUzJkz1aZNG82ZM0cPPPCA/ZjHH39cp06d0vjx45Wfn6+bbrpJq1evlq+vrxs7BwAAnsCtQUaS7rjjDt1xxx1V7rfZbJo5c6ZmzpxZi10BAAArcPtXFAAAANQUQQYAAFgWQQYAAFgWQQYAAFgWQQYAAFgWQQYAAFgWQQYAAFiW258jA3iizMxM5eXluaT2nj17XFIXAK5GBBngApmZmYqObq/i4tMuPU9pyVmX1geAqwFBBrhAXl6eiotPq9eYGQpoFen0+tm70rU79W2VlZU5vTYAXG0IMkAVAlpFKig8yul1C7MPO70mAFytWOwLAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsiyADAAAsq4G7GwBgLZmZmcrLy3NZ/ebNmys8PNxl9QHULQQZANWWmZmp6Oj2Ki4+7bJz+Pk11N69ewgzAKqFIAOg2vLy8lRcfFq9xsxQQKtIp9cvzD6srQueV15eHkEGQLUQZABctoBWkQoKj3J3GwDAYl8AAGBdBBkAAGBZbg0yzz33nGw2m8MWHR1t33/mzBklJCSoWbNm8vf3V3x8vHJzc93YMQAA8CRuvyLTsWNHZWdn27cvv/zSvm/q1Kn65JNPtHz5cm3atElZWVkaOnSoG7sFAACexO2LfRs0aKCQkJAK4wUFBZo/f74WL16s/v37S5JSUlLUvn17bdmyRb17967tVgEAgIdx+xWZAwcOKDQ0VNdee60eeOABZWZmSpIyMjJUWlqq2NhY+7HR0dEKDw9Xenq6u9oFAAAexK1XZHr16qWFCxcqKipK2dnZev7553XzzTdr9+7dysnJkbe3t5o0aeLwnuDgYOXk5FRZs6SkRCUlJfbXhYWFrmof8Gh79uyxRE0AuBJuDTKDBg2y/3OXLl3Uq1cvRUREaNmyZfLz86tRzaSkJD3//PPOahGwnOKCnyXZNGLECJedo7TkrMtqA8DlcPsamV9q0qSJfvWrX+ngwYO67bbbdPbsWeXn5ztclcnNza10Tc15iYmJmjZtmv11YWGhwsLCXNk24FFKT5+UZNT1/ifUok30JY+/HNm70rU79W2VlZU5tS4A1JRHBZmioiL9+9//1oMPPqgePXrIy8tLaWlpio+PlyTt27dPmZmZiomJqbKGj4+PfHx8aqtlwGP5twx3+tN3C7MPO7UeAFwptwaZ//3f/9Wdd96piIgIZWVlacaMGapfv77uu+8+BQYGauzYsZo2bZqCgoIUEBCgSZMmKSYmhjuWAACAJDcHmf/85z+677779PPPP6tFixa66aabtGXLFrVo0UKSNHv2bNWrV0/x8fEqKSlRXFyc5s6d686WAQCAB3FrkFmyZMlF9/v6+io5OVnJycm11BEAALAStz9HBgAAoKYIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLIIMgAAwLJqFGSuvfZa/fzzzxXG8/Pzde21115xUwAAANVRoyBz+PBhnTt3rsJ4SUmJfvzxxytuCgAAoDoaXM7Bqamp9n9es2aNAgMD7a/PnTuntLQ0RUZGOq05AACAi7msIDNkyBBJks1m08iRIx32eXl5KTIyUq+99prTmgMAALiYywoy5eXlkqQ2bdpo27Ztat68uUuaAgAAqI7LCjLnHTp0yNl9AAAAXLYaBRlJSktLU1pamo4dO2a/UnPeggULLrveyy+/rMTERD366KOaM2eOJOnMmTN67LHHtGTJEpWUlCguLk5z585VcHBwTdsGAAB1SI3uWnr++ec1cOBApaWlKS8vTydOnHDYLte2bdv017/+VV26dHEYnzp1qj755BMtX75cmzZtUlZWloYOHVqTlgEAQB1Uoysy8+bN08KFC/Xggw9ecQNFRUV64IEH9M477+iFF16wjxcUFGj+/PlavHix+vfvL0lKSUlR+/bttWXLFvXu3fuKzw0AAKytRldkzp49qxtvvNEpDSQkJGjw4MGKjY11GM/IyFBpaanDeHR0tMLDw5Wenl5lvZKSEhUWFjpsAACgbqpRkBk3bpwWL158xSdfsmSJvv76ayUlJVXYl5OTI29vbzVp0sRhPDg4WDk5OVXWTEpKUmBgoH0LCwu74j4BAIBnqtGvls6cOaO3335b69atU5cuXeTl5eWwf9asWZescfToUT366KNau3atfH19a9JGpRITEzVt2jT768LCQsIMAAB1VI2CzM6dO9W1a1dJ0u7dux322Wy2atXIyMjQsWPH1L17d/vYuXPntHnzZr355ptas2aNzp49q/z8fIerMrm5uQoJCamyro+Pj3x8fKo/GQAAYFk1CjIbNmy44hMPGDBAu3btchgbPXq0oqOj9cQTTygsLExeXl5KS0tTfHy8JGnfvn3KzMxUTEzMFZ8fAABYX42fI3OlGjdurE6dOjmMNWrUSM2aNbOPjx07VtOmTVNQUJACAgI0adIkxcTEcMcSAACQVMMgc+utt170V0jr16+vcUO/NHv2bNWrV0/x8fEOD8QDAACQahhkzq+POa+0tFQ7duzQ7t27K3yZ5OXYuHGjw2tfX18lJycrOTm5xjUBAEDdVaMgM3v27ErHn3vuORUVFV1RQwAAANVVo+fIVGXEiBE1+p4lAACAmnBqkElPT3fqM2EAAAAupka/WrrwixuNMcrOztb27dv1zDPPOKUxAACAS6lRkAkMDHR4Xa9ePUVFRWnmzJkaOHCgUxoDAAC4lBoFmZSUFGf3AQAAcNmu6IF4GRkZ2rNnjySpY8eO6tatm1OaAgAAqI4aBZljx45p+PDh2rhxo/17kPLz83XrrbdqyZIlatGihTN7BAAAqFSN7lqaNGmSTp48qe+++07Hjx/X8ePHtXv3bhUWFmry5MnO7hEAAKBSNbois3r1aq1bt07t27e3j3Xo0EHJycks9gUAALWmRldkysvL5eXlVWHcy8tL5eXlV9wUAABAddQoyPTv31+PPvqosrKy7GM//vijpk6dqgEDBjitOQAAgIupUZB58803VVhYqMjISF133XW67rrr1KZNGxUWFuqNN95wdo8AAACVqtEambCwMH399ddat26d9u7dK0lq3769YmNjndocAADAxVzWFZn169erQ4cOKiwslM1m02233aZJkyZp0qRJ6tmzpzp27KgvvvjCVb0CAAA4uKwgM2fOHD388MMKCAiosC8wMFATJkzQrFmznNYcAADAxVzWr5a+/fZb/elPf6py/8CBA/Xqq69ecVMA4CqZmZnKy8tzWf3mzZsrPDzcZfUBOLqsIJObm1vpbdf2Yg0a6KeffrripgDAFTIzMxUd3V7Fxadddg4/v4bau3cPYQaoJZcVZK655hrt3r1bbdu2rXT/zp071apVK6c0BgDOlpeXp+Li0+o1ZoYCWkU6vX5h9mFtXfC88vLyCDJALbmsIPOb3/xGzzzzjG6//Xb5+vo67CsuLtaMGTN0xx13OLVBAHC2gFaRCgqPcncbAJzgsoLM9OnT9dFHH+lXv/qVJk6cqKio/34Q7N27V8nJyTp37pyefvpplzQKAABwocsKMsHBwfrnP/+pRx55RImJiTLGSJJsNpvi4uKUnJys4OBglzQKAABwoct+IF5ERIQ+/fRTnThxQgcPHpQxRu3atVPTpk1d0R8AAECVavRkX0lq2rSpevbs6cxeAAAALkuNvmsJAADAExBkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZRFkAACAZbk1yLz11lvq0qWLAgICFBAQoJiYGH322Wf2/WfOnFFCQoKaNWsmf39/xcfHKzc3140dAwAAT+LWINO6dWu9/PLLysjI0Pbt29W/f3/dfffd+u677yRJU6dO1SeffKLly5dr06ZNysrK0tChQ93ZMgAA8CAN3HnyO++80+H1iy++qLfeektbtmxR69atNX/+fC1evFj9+/eXJKWkpKh9+/basmWL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AnTLLbeouNj539njatWZb05Ojh588EGFhISoUaNG6t69u/7v//7PTR1fmbfeektdunSxPwQuJiZGn332mX1/XfqsOu9ic65rn1fVRZC5hFOnTun6669XcnJypfunTZum1atX6/3339eePXs0ZcoUTZw4UampqbXcqXNs2rRJCQkJ2rJli9auXavS0lINHDhQp06dsh8zdepUffLJJ1q+fLk2bdqkrKwsDR061I1d19yl5puVlaWsrCy9+uqr2r17txYuXKjVq1dr7Nixbu68Zqrz8z1vzpw5Tv1aD3eoznzT09N1++23a+DAgfrXv/6lbdu2aeLEiapXz3ofj9WZ70MPPaR9+/YpNTVVu3bt0tChQzVs2DB98803buy8Zlq3bq2XX35ZGRkZ2r59u/r376+7775b3333naS69Vl13sXmXNc+r6rNKd/ueJWQZFasWOEw1rFjRzNz5kyHse7du5unn366FjtznWPHjhlJZtOmTcYYY/Lz842Xl5dZvny5/Zg9e/YYSSY9Pd1dbTrNhfOtzLJly4y3t7cpLS2txc5co6r5fvPNN+aaa64x2dnZlf53b1WVzbdXr15m+vTpbuzKdSqbb6NGjcx7773ncFxQUJB55513ars9l2jatKn529/+Vuc/q37p/JwrU5c+r6pivb9yeJgbb7xRqamp+vHHH2WM0YYNG7R//34NHDjQ3a05xflLkkFBQZKkjIwMlZaWKjY21n5MdHS0wsPDlZ6e7pYenenC+VZ1TEBAgBo0sMTzJC+qsvmePn1a999/v5KTk6v8clarunC+x44d09atW9WyZUvdeOONCg4OVt++ffXll1+6s02nqezne+ONN2rp0qU6fvy4ysvLtWTJEp05c0b9+vVzU5fOce7cOS1ZskSnTp1STExMnf+skirOuTJ16fOqSu5OUlaiSv5meubMGfPQQw8ZSaZBgwbG29vbvPvuu+5p0MnOnTtnBg8ebPr06WMf++CDD4y3t3eFY3v27Gkef/zx2mzP6Sqb74V++uknEx4ebp566qla7Mw1qprv+PHjzdixY+2vK/vv3ooqm296erqRZIKCgsyCBQvM119/baZMmWK8vb3N/v373djtlavq53vixAkzcOBA+2dWQECAWbNmjZu6vHI7d+40jRo1MvXr1zeBgYFm1apVxpi6/VlV1ZwvVJc+ry6mDke02vHGG29oy5YtSk1NVUREhDZv3qyEhASFhoY6/E3AihISErR79+4687fTS7nUfAsLCzV48GB16NBBzz33XO025wKVzTc1NVXr16+35HqJS6lsvuXl5ZKkCRMm2L+Itlu3bkpLS9OCBQuUlJTkll6doar/np955hnl5+dr3bp1at68uVauXKlhw4bpiy++UOfOnd3Ubc1FRUVpx44dKigo0IcffqiRI0dq06ZN7m7Lpaqac4cOHezH1LXPq4tyd5KyEl3wN9PTp08bLy8v849//MPhuLFjx5q4uLha7s65EhISTOvWrc0PP/zgMJ6WlmYkmRMnTjiMh4eHm1mzZtVih85V1XzPKywsNDExMWbAgAGmuLi4lrtzvqrm++ijjxqbzWbq169v3ySZevXqmb59+7qnWSeoar4//PCDkWQWLVrkMD5s2DBz//3312aLTlXVfA8ePGgkmd27dzuMDxgwwEyYMKE2W3SZAQMGmPHjx9fZz6rKnJ/zeXXt8+pSWCNzBUpLS1VaWlrh7ob69evb/6ZnNcYYTZw4UStWrND69evVpk0bh/09evSQl5eX0tLS7GP79u1TZmZmlb+j9WSXmq/037/ZDBw4UN7e3kpNTZWvr68bOnWOS833ySef1M6dO7Vjxw77JkmzZ89WSkqKGzq+Mpeab2RkpEJDQyvcorx//35FRETUZqtOcan5nj59WpLq1GfWhcrLy1VSUlLnPqsu5vycpbr1eVVtbo1RFnDy5EnzzTffmG+++cZIMrNmzTLffPONOXLkiDHGmL59+5qOHTuaDRs2mB9++MGkpKQYX19fM3fuXDd3XjOPPPKICQwMNBs3bjTZ2dn27fTp0/Zjfve735nw8HCzfv16s337dhMTE2NiYmLc2HXNXWq+BQUFplevXqZz587m4MGDDseUlZW5ufvLV52f74Vk4TUy1Znv7NmzTUBAgFm+fLk5cOCAmT59uvH19TUHDx50Y+c1c6n5nj171rRt29bcfPPNZuvWrebgwYPm1VdfNTabrcp1Fp7sySefNJs2bTKHDh0yO3fuNE8++aSx2Wzm888/N8bUrc+q8y4257r2eVVdBJlL2LBhg5FUYRs5cqQxxpjs7GwzatQoExoaanx9fU1UVJR57bXXTHl5uXsbr6HK5irJpKSk2I8pLi42v//9703Tpk1Nw4YNzf/8z/+Y7Oxs9zV9BS4136p+/pLMoUOH3Np7TVTn51vZe6waZKo736SkJNO6dWvTsGFDExMTY7744gv3NHyFqjPf/fv3m6FDh5qWLVuahg0bmi5dulS4HdsqxowZYyIiIoy3t7dp0aKFGTBggD3EGFO3PqvOu9ic69rnVXXZjDHG2Vd5AAAAagNrZAAAgGURZAAAgGURZAAAgGURZAAAgGURZAAAgGURZAAAgGURZAAAgGURZAAAgGURZAB4pPT0dNWvX1+DBw92dysAPBhP9gXgkcaNGyd/f3/Nnz9f+/btU2hoqLtbAuCBuCIDwOMUFRVp6dKleuSRRzR48GAtXLjQYX9qaqratWsnX19f3XrrrXr33Xdls9mUn59vP+bLL7/UzTffLD8/P4WFhWny5Mk6depU7U4EgMsRZAB4nGXLlik6OlpRUVEaMWKEFixYoPMXjw8dOqR77rlHQ4YM0bfffqsJEybo6aefdnj/v//9b91+++2Kj4/Xzp07tXTpUn355ZeaOHGiO6YDwIX41RIAj9OnTx8NGzZMjz76qMrKytSqVSstX75c/fr105NPPqlVq1Zp165d9uOnT5+uF198USdOnFCTJk00btw41a9fX3/961/tx3z55Zfq27evTp06JV9fX3dMC4ALcEUGgEfZt2+f/vWvf+m+++6TJDVo0ED33nuv5s+fb9/fs2dPh/fccMMNDq+//fZbLVy4UP7+/vYtLi5O5eXlOnToUO1MBECtaODuBgDgl+bPn6+ysjKHxb3GGPn4+OjNN9+sVo2ioiJNmDBBkydPrrAvPDzcab0CcD+CDACPUVZWpvfee0+vvfaaBg4c6LBvyJAh+vvf/66oqCh9+umnDvu2bdvm8Lp79+76/vvv1bZtW5f3DMC9WCMDwGOsXLlS9957r44dO6bAwECHfU888YTWr1+vZcuWKSoqSlOnTtXYsWO1Y8cOPfbYY/rPf/6j/Px8BQYGaufOnerdu7fGjBmjcePGqVGjRvr++++1du3aal/VAWANrJEB4DHmz5+v2NjYCiFGkuLj47V9+3adPHlSH374oT766CN16dJFb731lv2uJR8fH0lSly5dtGnTJu3fv18333yzunXrpmeffZZn0QB1EFdkAFjeiy++qHnz5uno0aPubgVALWONDADLmTt3rnr27KlmzZrpq6++0iuvvMIzYoCrFEEGgOUcOHBAL7zwgo4fP67w8HA99thjSkxMdHdbANyAXy0BAADLYrEvAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwrP8HgKs4zeht6IMAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=df, x='Age')\n",
    "plt.title('Distribution of Age')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70214456-61c2-4e4d-a1e3-8608aaf32113",
   "metadata": {},
   "source": [
    "## Categorical encoding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "47e84922-ee99-42f7-b9d0-829c07a4a9cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.compose import ColumnTransformer\n",
    "\n",
    "# Data normalization\n",
    "num_pipeline = Pipeline([\n",
    "        (\"scaler\", StandardScaler())\n",
    "    ])\n",
    "\n",
    "# Categorical Encoding\n",
    "cat_pipeline = Pipeline([\n",
    "        (\"ordinal_encoder\", OrdinalEncoder()), \n",
    "        (\"cat_encoder\", OneHotEncoder(sparse_output=False)),\n",
    "    ])\n",
    "\n",
    "num_attribs = [\"Age\", \"Family size\", \"latitude\", \"longitude\", \"Pin code\"]\n",
    "cat_attribs = [\"Gender\", \"Marital Status\", \"Occupation\", \"Monthly Income\", \"Educational Qualifications\", \"Output\", \"Unnamed: 12\"]\n",
    "\n",
    "preprocess_pipeline = ColumnTransformer([\n",
    "        (\"num\", num_pipeline, num_attribs),\n",
    "        (\"cat\", cat_pipeline, cat_attribs),\n",
    "    ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "75220f34-7ef3-4ad6-ab42-ad2a90d5a619",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X = preprocess_pipeline.fit_transform(df.drop(['Feedback'], axis=1))\n",
    "y = df['Feedback']\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "500e00e2-63ec-4418-8176-ca99e6b4b9bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cross-validation accuracy: 87.07%\n"
     ]
    }
   ],
   "source": [
    "#import random forest classifier\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.model_selection import cross_val_score\n",
    "\n",
    "rf_clf = RandomForestClassifier(random_state=42)\n",
    "cv_score = cross_val_score(rf_clf , X_train, y_train, cv=3)\n",
    "cv_score.mean()\n",
    "print(f\"Cross-validation accuracy: {cv_score.mean():.2%}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2b516866-e7c8-4bfc-ae0b-471d3a9a4be6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Precision: 91.54%\n",
      "Recall: 92.25%\n",
      "F1 Score: 91.89%\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import precision_score, recall_score, f1_score\n",
    "\n",
    "rf_clf.fit(X_train, y_train)\n",
    "y_pred = rf_clf.predict(X_test)\n",
    "\n",
    "precision = precision_score(y_test, y_pred, pos_label='Positive')\n",
    "recall = recall_score(y_test, y_pred, pos_label='Positive')\n",
    "f1 = f1_score(y_test, y_pred, pos_label='Positive')\n",
    "\n",
    "print(f\"Precision: {precision:.2%}\")\n",
    "print(f\"Recall: {recall:.2%}\")\n",
    "print(f\"F1 Score: {f1:.2%}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "253366cc-5d0a-453c-a9d0-9fead5049811",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plot model performance\n",
    "from sklearn.metrics import ConfusionMatrixDisplay\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "ConfusionMatrixDisplay.from_estimator(rf_clf, X_test, y_test)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "472ce467-b58c-4871-8ebb-49f8adcbca35",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
