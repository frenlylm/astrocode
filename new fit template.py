import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "DejaVu Serif"
serif = "DejaVu Serif"

#all code needed to change is here!
filename = r"filepath"
ObsID = "ObsID  = "
C, N, O = ["$C = $", "$N = $", "$O = $"]
HEII = "HEII 0"
norm1, norm2, norm3, norm4, norm5, norm6 = []
sigma, cstat, bins, flux = ["$sigma = $", "$cstat = $", "$N = $", "$flux = $"]
save_path_meg = r"C:\Users\fmeza\Downloads\research data\yoursavepathmeg.png"
save_path_heg = r"C:\Users\fmeza\Downloads\research data\yoursavepathheg.png"
save_path_both = r"C:\Users\fmeza\Downloads\research data\yoursavepathboth.png"

def readfile(filename):
    with open(filename, "r") as datfile:
        line = datfile.readline().strip()

        while line and line[0] not in "0123456789":
            line = datfile.readline().strip()

        data = []
        eg = [[], [], [], [], []]

        while line:
            if line[0] == "N":
                data.append(eg)
                eg = [[], [], [], [], []]
            else:
                line = line.split()
                eg[0].append(float(line[0]))  # Wavelength
                eg[1].append(float(line[1]))  # Bin width
                eg[2].append(float(line[2]))  # Data value
                eg[3].append(float(line[3]))  # Error bar
                eg[4].append(float(line[4]))  # Model value
            
            line = datfile.readline().strip()

        data.append(eg)  

    for spectrum in data:
        if spectrum[0] and spectrum[0][0] > spectrum[0][1]:
            for i in range(5):
                spectrum[i].reverse()

    return data

def histogramdata(data):
    histwvs = [[], []]
    histmods = [[], []]
    histvals = [[], []]

    for i in range(len(data)):
        for j in range(len(data[i][1])):
            histwvs[i].extend([data[i][0][j] - data[i][1][j], data[i][0][j] + data[i][1][j]])
            histvals[i].extend([data[i][2][j]] * 2)
            histmods[i].extend([data[i][4][j]] * 2)

    return histwvs, histvals, histmods

data = readfile(filename)
histwvs, histvals, histmods = histogramdata(data)
megwvs, megbins, megvals, megerrors, megmods = data[0]
hegwvs, hegbins, hegvals, hegerrors, hegmods = data[1]

def meg_action():
    plt.figure(figsize=(18, 8))
    plt.xlim(5, 17.5)
    plt.ylim(0, .2)
    plt.plot(histwvs[0], histmods[0], color='green', linewidth=3, label = "model")
    plt.errorbar(megwvs, megvals, xerr=megbins, yerr=megerrors, fmt='.', alpha=0.4, color='blue', linewidth=1.5, label = "data")
    plt.annotate(f'ζ pup MEG group10 {HEII}', xy=(13, .15), xytext=(5.1, .19), fontsize = 19)
    plt.annotate(ObsID, xy=(13, .15), xytext=(5.1, .17), fontsize = 17, fontname = 'serif')
    plt.annotate(C, xy=(13, .06), xytext=(9, .19), fontsize = 17, fontname = 'serif')
    plt.annotate(N, xy=(13, .06), xytext=(10.5, .19), fontsize = 17, fontname = 'serif')
    plt.annotate(O, xy=(13, .06), xytext=(12, .19), fontsize = 17, fontname = 'serif')
    plt.annotate(f"$norm_1 = {norm1}$", xy=(13, .15), xytext=(14, 0.19), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_2 = {norm2}$", xy=(13, 0.18), xytext=(14, 0.175), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_3 = {norm3}$", xy=(13, .145), xytext=(14, 0.16), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_4 = {norm4}$", xy=(13, .135), xytext=(14, .145), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_5 = {norm5}$", xy=(13, .13), xytext=(14, .13), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_6 = {norm6}$", xy=(13, .145), xytext=(14, .115), fontsize = 19, fontname = 'serif')
    plt.annotate(sigma, xy=(13, .145), xytext=(14, .1), fontsize = 19, fontname = 'serif')
    plt.annotate(cstat, xy=(13, .14), xytext=(14, .085), fontsize = 19, fontname = 'serif')
    plt.annotate(bins, xy=(13, .13), xytext=(16.3, .085), fontsize = 19, fontname = 'serif')
    plt.annotate(flux, xy=(13, .055), xytext=(14, .07), fontsize = 19, fontname = 'serif')
    plt.xlabel('Wavelength (Å)', fontsize = 19, fontname = 'serif')
    plt.ylabel('Counts (s$^{-1}$ Å$^{-1}$)', fontsize = 19, fontname = 'serif')
    plt.savefig(save_path_meg)
    plt.show()

def heg_action():
    plt.figure(figsize=(18, 8))
    plt.xlim(4.7, 13)
    plt.ylim(0, .12)
    plt.plot(histwvs[1], histmods[1], color='orange', linewidth=2, label = "model")
    plt.errorbar(hegwvs, hegvals, xerr=hegbins, yerr=hegerrors, fmt='.', alpha=1, color='gray', linewidth=2)
    plt.annotate(f'ζ pup HEG group10 {HEII}', xy=(13, .115), xytext=(4.8, .115), fontsize = 19, fontname = 'serif')
    plt.annotate(ObsID, xy=(13, .076), xytext=(4.8, .1), fontsize = 19, fontname = 'serif')
    plt.annotate(C, xy=(13, .06), xytext=(7.5, .115), fontsize = 17, fontname = 'serif')
    plt.annotate(N, xy=(13, .06), xytext=(8.5, .115), fontsize = 17, fontname = 'serif')
    plt.annotate(O, xy=(13, .06), xytext=(9.5, .115), fontsize = 17, fontname = 'serif')
    plt.annotate(f"$norm_1 = {norm1}$", xy=(10, .075), xytext=(11, .115), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_2 = {norm2}$", xy=(13, 0.08), xytext=(11, 0.105), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_3 = {norm3}$", xy=(13, .075), xytext=(11, 0.095), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_4 = {norm4}$", xy=(13, .07), xytext=(11, .085), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_5 = {norm5}$", xy=(13, .065), xytext=(11, .075), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_6 = {norm6}$", xy=(13, .06), xytext=(11, .065), fontsize = 19, fontname = 'serif')
    plt.annotate(sigma, xy=(13, .055), xytext=(11, .055), fontsize = 19, fontname = 'serif')
    plt.annotate(cstat, xy=(13, .05), xytext=(11, .045), fontsize = 19, fontname = 'serif')
    plt.annotate(bins, xy=(13, .05), xytext=(12.3, .045), fontsize = 19, fontname = 'serif')
    plt.annotate(flux, xy=(13, .055), xytext=(11, 0.035), fontsize = 19, fontname = 'serif')
    plt.xlabel('Wavelength (Å)', fontsize = 19, fontname = 'serif')
    plt.ylabel('Counts (s$^{-1}$ Å$^{-1}$)', fontsize = 19, fontname = 'serif')
    plt.savefig(save_path_heg)
    plt.show()
    
def both_action():
    plt.figure(figsize=(18, 8))
    plt.xlim(5, 17.5)
    plt.ylim(0, .2)
    #meg plot
    plt.plot(histwvs[0], histmods[0], color='green', linewidth=3, label = "model")
    plt.errorbar(megwvs, megvals, xerr=megbins, yerr=megerrors, fmt='.', alpha=0.4, color='blue', linewidth=1.5, label = "data")
    #heg plot
    plt.plot(histwvs[1], histmods[1], color='orange', linewidth=4, label = "model")
    plt.errorbar(hegwvs, hegvals, xerr=hegbins, yerr=hegerrors, fmt='.', alpha=0.4, color='gray', linewidth=2)
    #annotations
    plt.annotate(f'ζ pup group10 {HEII}'f'ζ pup group10 {HEII}', xy=(13, .15), xytext=(5.1, .19), fontsize = 19, fontname = 'serif')
    plt.annotate(ObsID, xy=(13, .15), xytext=(5.1, .17), fontsize = 19, fontname = 'serif')
    plt.annotate(C, xy=(13, .06), xytext=(9, .19), fontsize = 17, fontname = 'serif')
    plt.annotate(N, xy=(13, .06), xytext=(10.5, .19), fontsize = 17, fontname = 'serif')
    plt.annotate(O, xy=(13, .06), xytext=(12, .19), fontsize = 17, fontname = 'serif')
    plt.annotate(f"$norm_1 = {norm1}$", xy=(13, .15), xytext=(14, 0.19), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_2 = {norm2}$", xy=(13, 0.18), xytext=(14, 0.175), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_3 = {norm3}$", xy=(13, .145), xytext=(14, 0.16), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_4 = {norm4}$", xy=(13, .135), xytext=(14, .145), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_5 = {norm5}$", xy=(13, .13), xytext=(14, .13), fontsize = 19, fontname = 'serif')
    plt.annotate(f"$norm_6 = {norm6}$", xy=(13, .145), xytext=(14, .115), fontsize = 19, fontname = 'serif')
    plt.annotate(sigma, xy=(13, .145), xytext=(14, .1), fontsize = 19, fontname = 'serif')
    plt.annotate(cstat, xy=(13, .14), xytext=(14, .085), fontsize = 19, fontname = 'serif')
    plt.annotate(bins, xy=(13, .13), xytext=(16.3, .085), fontsize = 19, fontname = 'serif')
    plt.annotate(flux, xy=(13, .055), xytext=(14, .07), fontsize = 19, fontname = 'serif')
    plt.xlabel('Wavelength (Å)', fontsize = 19, fontname = 'serif')
    plt.ylabel('Counts (s$^{-1}$ Å$^{-1}$)', fontsize = 19, fontname = 'serif')
    plt.savefig(save_path_both)
    plt.show()

meg_action()    
heg_action()    
both_action()

#you have an option to have a user input, in case you would prefer to load the graphs in one at a time 
#just delete the '''s below and the above function calls, but this is not necessary.

'''
choice = input("Do you want 'meg', 'heg', or 'both'? ").strip().lower()

if choice == "meg":
    meg_action()
elif choice == "heg":
    heg_action()
elif choice == "both":
    both_action()
else:
    print("Invalid choice. Please enter 'meg', 'heg', or 'both'.")
'''