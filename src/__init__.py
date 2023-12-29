import pandas as pd
from plotnine import *

def plot_roc_curve(fpr, tpr, thresholds) -> ggplot:
    roc_df = pd.DataFrame.from_dict({"FPR": fpr, "TPR": tpr, "Threshold": thresholds})
    plot = (
        ggplot(roc_df, aes(x='FPR', y='TPR', color='Threshold')) +
        geom_line() +
        geom_point() +
        scale_color_gradient(low = "blue", high = "red") +
        labs(title='Receiver Operating Characteristic', x='False Positive Rate', y='True Positive Rate', color='Threshold') +
        geom_line(aes(x='FPR', y='FPR'), color="black", linetype='dashed')
    )
    return plot