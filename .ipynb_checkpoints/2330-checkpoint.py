{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dd9c0495",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import matplotlib.pyplot as plt\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2b03a932",
   "metadata": {},
   "outputs": [],
   "source": [
    "fn = 'FMNPTK_2330.csv'\n",
    "with open (fn) as csvFile:\n",
    "    csvReader = csv.reader(csvFile)\n",
    "    listCsv = list(csvReader)\n",
    "    csvData = listCsv[2:-5]\n",
    "    years, highs, lows, prices = [],[], [], []\n",
    "    for row in csvData:\n",
    "        try:\n",
    "            year = int(row[0]) + 1911\n",
    "            high = float(row[4])\n",
    "            low = float(row[6])\n",
    "            price = float(row[8])\n",
    "        except Exception:\n",
    "            print('有少值')\n",
    "        else:\n",
    "            years.append(year)\n",
    "            highs.append(high)\n",
    "            lows.append(low)\n",
    "            prices.append(price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7c0cf63f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[106.0,\n",
       " 173.0,\n",
       " 173.0,\n",
       " 171.0,\n",
       " 222.0,\n",
       " 105.5,\n",
       " 97.5,\n",
       " 72.5,\n",
       " 68.5,\n",
       " 64.3,\n",
       " 70.0,\n",
       " 73.1,\n",
       " 69.8,\n",
       " 65.2,\n",
       " 75.0,\n",
       " 78.3,\n",
       " 99.4,\n",
       " 116.5,\n",
       " 142.0,\n",
       " 155.0,\n",
       " 193.0]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "highs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e52fa82c",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Illegal format string \"_*\"; two marker symbols",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-15-fe1dc8ad9e43>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mfig\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfigure\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdpi\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m80\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfigsize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m8\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0myears\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhighs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'_*'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlabel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'High'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0myears\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlows\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'_o'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlabel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'Low'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0myears\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mprices\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'_*'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlabel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'Price'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlegend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mloc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'Best'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\matplotlib\\pyplot.py\u001b[0m in \u001b[0;36mplot\u001b[1;34m(scalex, scaley, data, *args, **kwargs)\u001b[0m\n\u001b[0;32m   2838\u001b[0m \u001b[1;33m@\u001b[0m\u001b[0m_copy_docstring_and_deprecators\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mAxes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2839\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscalex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscaley\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2840\u001b[1;33m     return gca().plot(\n\u001b[0m\u001b[0;32m   2841\u001b[0m         \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscalex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mscalex\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscaley\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mscaley\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2842\u001b[0m         **({\"data\": data} if data is not None else {}), **kwargs)\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\matplotlib\\axes\\_axes.py\u001b[0m in \u001b[0;36mplot\u001b[1;34m(self, scalex, scaley, data, *args, **kwargs)\u001b[0m\n\u001b[0;32m   1741\u001b[0m         \"\"\"\n\u001b[0;32m   1742\u001b[0m         \u001b[0mkwargs\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcbook\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnormalize_kwargs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmlines\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mLine2D\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1743\u001b[1;33m         \u001b[0mlines\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_lines\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1744\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mlines\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1745\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_line\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mline\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\matplotlib\\axes\\_base.py\u001b[0m in \u001b[0;36m__call__\u001b[1;34m(self, data, *args, **kwargs)\u001b[0m\n\u001b[0;32m    271\u001b[0m                 \u001b[0mthis\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    272\u001b[0m                 \u001b[0margs\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 273\u001b[1;33m             \u001b[1;32myield\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_plot_args\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mthis\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    274\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    275\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mget_next_color\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\matplotlib\\axes\\_base.py\u001b[0m in \u001b[0;36m_plot_args\u001b[1;34m(self, tup, kwargs)\u001b[0m\n\u001b[0;32m    367\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_plot_args\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtup\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    368\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtup\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m1\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtup\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 369\u001b[1;33m             \u001b[0mlinestyle\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmarker\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcolor\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_process_plot_format\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtup\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    370\u001b[0m             \u001b[0mtup\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtup\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    371\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtup\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m3\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\matplotlib\\axes\\_base.py\u001b[0m in \u001b[0;36m_process_plot_format\u001b[1;34m(fmt)\u001b[0m\n\u001b[0;32m    144\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mc\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mmlines\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlineMarkers\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    145\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mmarker\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 146\u001b[1;33m                 raise ValueError(\n\u001b[0m\u001b[0;32m    147\u001b[0m                     'Illegal format string \"%s\"; two marker symbols' % fmt)\n\u001b[0;32m    148\u001b[0m             \u001b[0mmarker\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mc\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Illegal format string \"_*\"; two marker symbols"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 960x640 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure(dpi=80, figsize=(12, 8))\n",
    "plt.plot(years, highs, '_*', label='High')\n",
    "plt.plot(years, lows, '_o', label='Low')\n",
    "plt.plot(years, prices, '_*', label='Price')\n",
    "plt.legend(loc='Best')\n",
    "fig.autofmt_xdate()\n",
    "plt.title(\"Taiwan Cement Company\", fontsize=24)\n",
    "plt.xlabel(\"\", fontsize=14)\n",
    "plt.xlabel(\"\", fontsize=14)\n",
    "plt.tick_params(axis=\"Both\", labelsize=12, color='red')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab5457b7",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
