import  matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import numpy as np
import urllib
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style
style.use('ggplot')
# UNIX TIME---NUMBER OF SECONDS AFTER 1ST JANUARY 1970

def bytespdate2num(format,encoding='utf-8'):
    strconverter=mdates.strpdate2num(format) #strip date to number function from mdates
    def bytesconverter(b):
        s=b.decode(encoding)
        return strconverter(s)
    return bytesconverter

MA1=5
MA2=10
def moving_avg(values,window):
    weights=np.repeat(1.0,window)/window
    smas=np.convolve(values,weights,'valid')
    return smas

def high_low(highs,lows):
    return highs-lows





def graph_data(stock):
    fig=plt.figure(facecolor='#f0f0f0')
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1,colspan=1)
    plt.title('STOCK SCREENER\n NAIROBI SECURITIES EXCHANGE')
    plt.ylabel('High-Low')
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4,colspan=1,sharex=ax1) # sharex allows sharing of the x axis by the specified subgrid
    plt.ylabel('PRICE (Ksh)')
    ax2v=ax2.twinx() # define a new axis that will be a twin of the ax2 x axis ie, they will share the x axis
    ax2v.grid(False) # to avoid double grids on the same axes
    ax2v.axes.yaxis.set_ticklabels([])

    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1,colspan=1,sharex=ax1)
    plt.xlabel('Dates')
    plt.ylabel('Moving Avg')


    stock_price_url='http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    #source_code=urllib.request.urlopen(stock_price_url).read().decode()
    stock_data=[]
    # split_source=source_code.split('\n')
    # for line in split_source:
    #     split_line=line.split(',') # to determine the length of the lines for filtering out data that is not required
    #     if len(split_line)== 6:
    #         if 'values' not in line and 'labels' not in line:
    #             stock_data.append(line)

    date,openp,highp,lowp,closep,volume=np.loadtxt('ohlctest.txt',delimiter=',',unpack=True,
                                                 converters={0:bytespdate2num('%Y%m%d')})
    ma1 = moving_avg(closep, MA1)
    ma2 = moving_avg(closep, MA2)
    start = len(date[MA2 - 1:])
    h_l = list(map(high_low, highp, lowp))
    # map function ....takes the second and third argument and maps them into the parameters of the first argument which is the function
    x=0
    ohlc=[]
    while x < len(date):
        append_me=date[x],openp[x],highp[x],lowp[x],closep[x],volume[x] #retreive data in proper order for plotting purposes
        ohlc.append(append_me)
        x+=1
    candlestick_ohlc(ax2,ohlc[-start:],width=0.5,colorup='g',colordown='r')
    #plot volume
    ax2v.fill_between(date[-start:],0,volume[-start:],facecolor='#0079a3',alpha=0.4)
    ax2v.plot([],[],color='#0079a3',alpha=0.5,label='Volume') # labels cant be added to fills hence we use an empty line

    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(5))

    ax2v.set_ylim(0, 1 * volume.max()) # to ensure the volume graph doesnt take up much space

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax3.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(5))

    # remove the x axis ticks from sublot 1 and 2
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)

    # max number of labels is 5 and we prune lower lables to avoid overlap
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4,prune='lower'))
    # prunning upper ensures that values dont overflow upwards and thus overlap with other subplots.
    # it gives the max number as the upper limit
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=8, prune='upper'))
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))


    #sharing of the X axis between the 3 subplots

    # annotating the last price ie, the last closep
    bbox_props=dict(boxstyle='round',fc='c',ec='k',lw=1)
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]), xytext=(date[-1], closep[-1]),
                 bbox=bbox_props)


    ax1.plot_date(date[-start:],h_l[-start:],'-',label='H-L')
    ax3.plot(date[-start:],ma1[-start:],linewidth=1,label=(str(MA1)+'MA'))
    ax3.plot(date[-start:], ma2[-start:],linewidth=1,label=(str(MA2)+'MA'))

    ax3.fill_between(date[-start:],ma2[-start:],ma1[-start:],
                     where=(ma1[-start:]< ma2[-start:]),
                     facecolor='r',edgecolor='r',alpha=0.5
                     )
    #ax2.annotate('Bad news'
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:], # set the boundaries ie, the x axis and the bounds of the y axis
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolor='g', edgecolor='g', alpha=0.5
                     )
    # ax2.annotate('Bad news'
    # ,(date[9],closep[9]), xytext=(0.8,0.9), textcoords='axes fraction', arrowprops=dict(facecolor='grey', color='grey'))
    #xytext gives the position of the text as textcoords which is fraction of the axes hence 80% and 90% of the x and y coordinates
    # give the text and the coords of the poit itll point to i.e (date[9],closep[9])
    ax1.spines['left'].set_color('c')
    ax2v.spines['left'].set_color('c')
    ax3.spines['left'].set_color('c')
    ax3.spines['bottom'].set_color('c')

    ax2.spines['right'].set_visible(False)
    ax2v.spines['top'].set_visible(False)

    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax2v.spines['bottom'].set_visible(False)

    ax3.spines['right'].set_visible(False)
    ax3.spines['top'].set_visible(False)

    #Custom Legends
    ax1.legend()
    leg=ax1.legend(loc=9,ncol=2,prop={'size':11}) # loc is location ncol is num of columns
    leg.get_frame().set_alpha(0.4)

    ax2v.legend()
    leg = ax1.legend(loc=5, ncol=2, prop={'size': 11})
    leg.get_frame().set_alpha(0.4)

    ax3.legend()
    leg = ax1.legend(loc=9, ncol=2, prop={'size': 11})
    leg.get_frame().set_alpha(0.4)
    plt.show()
    fig.savefig('stockscreener.png',facecoloe=fig.get_facecolor())
graph_data('TSLA')
