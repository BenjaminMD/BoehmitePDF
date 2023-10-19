from ezfit import FitPDF, Contribution
from ezpdf import plot_PDF
from pathlib import Path


data_file = Path("data/gr/bf4_acc_r01.gr")

AlOOH = Contribution("AlOOH", "sphericalCF", "AlOOH")

fit = FitPDF(data_file, contributions=[AlOOH])

fit.shared_param("AlOOH", "O" "Biso")


fit.update_recipe()

#fit.LoadResFromFile("200.res")

fit.run_fit()

fit.dw.save_results(fit.recipe, "", "results", "200", fit.phases)