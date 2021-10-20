
Complete actionable model:
Only rules up to the selected node:

def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/616ff8349193b917380129f2

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] at UCI[*] Machine Learning Repository[*]
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI: http://cml.ics.uci.edu/
        [*]Machine Learning Repository: http://archive.ics.uci.edu/ml/index.html
    """
    if (glucose is None):
        return u'false'
    if (glucose > 122):
        if (glucose > 155):
            if (insulin is None):
                return u'true'
            if (insulin > 349):
                if (glucose > 169):
                    if (glucose > 191):
                        if (skinfold is None):
                            return u'false'
                        if (skinfold > 42):
                            return u'true'
                        if (skinfold <= 42):
                            return u'false'
                    if (glucose <= 191):
                        return u'true'
                if (glucose <= 169):
                    return u'false'
            if (insulin <= 349):
                if (diabetes_pedigree is None):
                    return u'true'
                if (diabetes_pedigree > 0.34494):
                    if (age is None):
                        return u'true'
                    if (age > 36):
                        if (pregnancies is None):
                            return u'true'
                        if (pregnancies > 6):
                            return u'true'
                        if (pregnancies <= 6):
                            if (diabetes_pedigree > 1.1565):
                                return u'false'
                            if (diabetes_pedigree <= 1.1565):
                                if (age > 50):
                                    return u'true'
                                if (age <= 50):
                                    if (bmi is None):
                                        return u'false'
                                    if (bmi > 33.95):
                                        return u'true'
                                    if (bmi <= 33.95):
                                        return u'false'
                    if (age <= 36):
                        return u'true'
                if (diabetes_pedigree <= 0.34494):
                    if (bmi is None):
                        return u'true'
                    if (bmi > 35.3):
                        if (age is None):
                            return u'true'
                        if (age > 26):
                            return u'true'
                        if (age <= 26):
                            return u'false'
                    if (bmi <= 35.3):
                        if (age is None):
                            return u'true'
                        if (age > 59):
                            return u'false'
                        if (age <= 59):
                            if (diabetes_pedigree > 0.2695):
                                if (diabetes_pedigree > 0.3005):
                                    if (blood_pressure is None):
                                        return u'true'
                                    if (blood_pressure > 76):
                                        if (diabetes_pedigree > 0.314):
                                            return u'false'
                                        if (diabetes_pedigree <= 0.314):
                                            return u'true'
                                    if (blood_pressure <= 76):
                                        return u'true'
                                if (diabetes_pedigree <= 0.3005):
                                    return u'false'
                            if (diabetes_pedigree <= 0.2695):
                                if (pregnancies is None):
                                    return u'true'
                                if (pregnancies > 9):
                                    if (blood_pressure is None):
                                        return u'false'
                                    if (blood_pressure > 66):
                                        return u'false'
                                    if (blood_pressure <= 66):
                                        return u'true'
                                if (pregnancies <= 9):
                                    return u'true'
        if (glucose <= 155):
            if (age is None):
                return u'false'
            if (age > 24):
                if (bmi is None):
                    return u'true'
                if (bmi > 29.9875):
                    if (glucose > 123):
                        if (diabetes_pedigree is None):
                            return u'true'
                        if (diabetes_pedigree > 0.72025):
                            if (bmi > 39.8):
                                if (bmi > 41.2):
                                    return u'true'
                                if (bmi <= 41.2):
                                    return u'false'
                            if (bmi <= 39.8):
                                return u'true'
                        if (diabetes_pedigree <= 0.72025):
                            if (age > 34):
                                if (diabetes_pedigree > 0.3965):
                                    if (diabetes_pedigree > 0.694):
                                        return u'false'
                                    if (diabetes_pedigree <= 0.694):
                                        return u'true'
                                if (diabetes_pedigree <= 0.3965):
                                    if (bmi > 45.55):
                                        return u'true'
                                    if (bmi <= 45.55):
                                        if (blood_pressure is None):
                                            return u'true'
                                        if (blood_pressure > 77):
                                            if (skinfold is None):
                                                return u'false'
                                            if (skinfold > 16):
                                                if (bmi > 37):
                                                    return u'false'
                                                if (bmi <= 37):
                                                    if (diabetes_pedigree > 0.3385):
                                                        return u'false'
                                                    if (diabetes_pedigree <= 0.3385):
                                                        return u'true'
                                            if (skinfold <= 16):
                                                return u'false'
                                        if (blood_pressure <= 77):
                                            if (blood_pressure > 30):
                                                if (insulin is None):
                                                    return u'true'
                                                if (insulin > 171):
                                                    return u'false'
                                                if (insulin <= 171):
                                                    return u'true'
                                            if (blood_pressure <= 30):
                                                return u'false'
                            if (age <= 34):
                                if (blood_pressure is None):
                                    return u'false'
                                if (blood_pressure > 59):
                                    if (diabetes_pedigree > 0.56):
                                        return u'false'
                                    if (diabetes_pedigree <= 0.56):
                                        if (diabetes_pedigree > 0.312):
                                            if (age > 28):
                                                if (skinfold is None):
                                                    return u'false'
                                                if (skinfold > 24):
                                                    return u'false'
                                                if (skinfold <= 24):
                                                    return u'true'
                                            if (age <= 28):
                                                return u'true'
                                        if (diabetes_pedigree <= 0.312):
                                            if (bmi > 31.05):
                                                return u'false'
                                            if (bmi <= 31.05):
                                                return u'true'
                                if (blood_pressure <= 59):
                                    return u'true'
                    if (glucose <= 123):
                        if (skinfold is None):
                            return u'false'
                        if (skinfold > 7):
                            return u'false'
                        if (skinfold <= 7):
                            return u'true'
                if (bmi <= 29.9875):
                    if (age > 54):
                        if (bmi > 24):
                            return u'false'
                        if (bmi <= 24):
                            if (bmi > 23):
                                return u'true'
                            if (bmi <= 23):
                                return u'false'
                    if (age <= 54):
                        if (age > 41):
                            if (age > 49):
                                if (bmi > 13):
                                    if (diabetes_pedigree is None):
                                        return u'false'
                                    if (diabetes_pedigree > 0.194):
                                        return u'false'
                                    if (diabetes_pedigree <= 0.194):
                                        return u'true'
                                if (bmi <= 13):
                                    return u'true'
                            if (age <= 49):
                                return u'true'
                        if (age <= 41):
                            if (bmi > 28.5):
                                return u'false'
                            if (bmi <= 28.5):
                                if (bmi > 26.15):
                                    if (diabetes_pedigree is None):
                                        return u'true'
                                    if (diabetes_pedigree > 0.48):
                                        return u'false'
                                    if (diabetes_pedigree <= 0.48):
                                        if (skinfold is None):
                                            return u'true'
                                        if (skinfold > 8):
                                            return u'true'
                                        if (skinfold <= 8):
                                            if (blood_pressure is None):
                                                return u'false'
                                            if (blood_pressure > 73):
                                                return u'false'
                                            if (blood_pressure <= 73):
                                                if (bmi > 27.25):
                                                    return u'true'
                                                if (bmi <= 27.25):
                                                    return u'false'
                                if (bmi <= 26.15):
                                    return u'false'
            if (age <= 24):
                if (bmi is None):
                    return u'false'
                if (bmi > 30.95):
                    if (insulin is None):
                        return u'false'
                    if (insulin > 260):
                        return u'false'
                    if (insulin <= 260):
                        if (glucose > 127):
                            if (insulin > 65):
                                return u'true'
                            if (insulin <= 65):
                                if (blood_pressure is None):
                                    return u'false'
                                if (blood_pressure > 85):
                                    return u'true'
                                if (blood_pressure <= 85):
                                    if (glucose > 136):
                                        return u'false'
                                    if (glucose <= 136):
                                        if (diabetes_pedigree is None):
                                            return u'false'
                                        if (diabetes_pedigree > 0.3025):
                                            if (bmi > 31.8):
                                                return u'false'
                                            if (bmi <= 31.8):
                                                return u'true'
                                        if (diabetes_pedigree <= 0.3025):
                                            return u'true'
                        if (glucose <= 127):
                            return u'false'
                if (bmi <= 30.95):
                    if (blood_pressure is None):
                        return u'false'
                    if (blood_pressure > 55):
                        return u'false'
                    if (blood_pressure <= 55):
                        if (bmi > 27.15):
                            return u'false'
                        if (bmi <= 27.15):
                            return u'true'
    if (glucose <= 122):
        if (bmi is None):
            return u'false'
        if (bmi > 25.82164):
            if (pregnancies is None):
                return u'false'
            if (pregnancies > 6):
                if (diabetes_pedigree is None):
                    return u'false'
                if (diabetes_pedigree > 0.776):
                    return u'true'
                if (diabetes_pedigree <= 0.776):
                    if (glucose > 101):
                        if (age is None):
                            return u'true'
                        if (age > 40):
                            if (bmi > 31.8):
                                if (bmi > 33.55):
                                    return u'false'
                                if (bmi <= 33.55):
                                    return u'true'
                            if (bmi <= 31.8):
                                return u'false'
                        if (age <= 40):
                            if (diabetes_pedigree > 0.1375):
                                return u'true'
                            if (diabetes_pedigree <= 0.1375):
                                return u'false'
                    if (glucose <= 101):
                        if (pregnancies > 11):
                            if (skinfold is None):
                                return u'false'
                            if (skinfold > 32):
                                return u'false'
                            if (skinfold <= 32):
                                if (blood_pressure is None):
                                    return u'true'
                                if (blood_pressure > 66):
                                    return u'true'
                                if (blood_pressure <= 66):
                                    return u'false'
                        if (pregnancies <= 11):
                            return u'false'
            if (pregnancies <= 6):
                if (bmi > 48.25):
                    return u'true'
                if (bmi <= 48.25):
                    if (age is None):
                        return u'false'
                    if (age > 39):
                        if (blood_pressure is None):
                            return u'false'
                        if (blood_pressure > 89):
                            return u'false'
                        if (blood_pressure <= 89):
                            if (skinfold is None):
                                return u'false'
                            if (skinfold > 27):
                                if (skinfold > 36):
                                    if (bmi > 37.2):
                                        return u'false'
                                    if (bmi <= 37.2):
                                        return u'true'
                                if (skinfold <= 36):
                                    return u'false'
                            if (skinfold <= 27):
                                if (diabetes_pedigree is None):
                                    return u'true'
                                if (diabetes_pedigree > 0.8365):
                                    return u'false'
                                if (diabetes_pedigree <= 0.8365):
                                    if (pregnancies > 4):
                                        if (bmi > 29.35):
                                            if (diabetes_pedigree > 0.38):
                                                if (bmi > 30.55):
                                                    return u'false'
                                                if (bmi <= 30.55):
                                                    return u'true'
                                            if (diabetes_pedigree <= 0.38):
                                                return u'true'
                                        if (bmi <= 29.35):
                                            return u'false'
                                    if (pregnancies <= 4):
                                        return u'true'
                    if (age <= 39):
                        if (bmi > 29.3625):
                            if (glucose > 92):
                                if (skinfold is None):
                                    return u'false'
                                if (skinfold > 37):
                                    if (diabetes_pedigree is None):
                                        return u'false'
                                    if (diabetes_pedigree > 0.8605):
                                        if (bmi > 39.1):
                                            return u'false'
                                        if (bmi <= 39.1):
                                            return u'true'
                                    if (diabetes_pedigree <= 0.8605):
                                        return u'false'
                                if (skinfold <= 37):
                                    if (bmi > 31.21875):
                                        if (bmi > 33.7):
                                            if (pregnancies > 3):
                                                return u'false'
                                            if (pregnancies <= 3):
                                                if (blood_pressure is None):
                                                    return u'false'
                                                if (blood_pressure > 82):
                                                    return u'true'
                                                if (blood_pressure <= 82):
                                                    if (diabetes_pedigree is None):
                                                        return u'false'
                                                    if (diabetes_pedigree > 0.6395):
                                                        if (insulin is None):
                                                            return u'true'
                                                        if (insulin > 125):
                                                            return u'true'
                                                        if (insulin <= 125):
                                                            if (insulin > 83):
                                                                return u'false'
                                                            if (insulin <= 83):
                                                                if (bmi > 44.1):
                                                                    return u'false'
                                                                if (bmi <= 44.1):
                                                                    return u'true'
                                                    if (diabetes_pedigree <= 0.6395):
                                                        if (glucose > 120):
                                                            if (blood_pressure > 68):
                                                                return u'false'
                                                            if (blood_pressure <= 68):
                                                                return u'true'
                                                        if (glucose <= 120):
                                                            return u'false'
                                        if (bmi <= 33.7):
                                            if (pregnancies > 1):
                                                if (diabetes_pedigree is None):
                                                    return u'false'
                                                if (diabetes_pedigree > 0.2135):
                                                    if (age > 27):
                                                        if (bmi > 32.1):
                                                            return u'true'
                                                        if (bmi <= 32.1):
                                                            return u'false'
                                                    if (age <= 27):
                                                        return u'false'
                                                if (diabetes_pedigree <= 0.2135):
                                                    return u'true'
                                            if (pregnancies <= 1):
                                                return u'true'
                                    if (bmi <= 31.21875):
                                        if (pregnancies > 3):
                                            if (blood_pressure is None):
                                                return u'false'
                                            if (blood_pressure > 65):
                                                return u'false'
                                            if (blood_pressure <= 65):
                                                return u'true'
                                        if (pregnancies <= 3):
                                            return u'false'
                            if (glucose <= 92):
                                if (age > 25):
                                    if (age > 27):
                                        return u'false'
                                    if (age <= 27):
                                        if (bmi > 38.9):
                                            return u'false'
                                        if (bmi <= 38.9):
                                            return u'true'
                                if (age <= 25):
                                    return u'false'
                        if (bmi <= 29.3625):
                            return u'false'
        if (bmi <= 25.82164):
            if (pregnancies is None):
                return u'false'
            if (pregnancies > 9):
                if (bmi > 11.55):
                    return u'false'
                if (bmi <= 11.55):
                    return u'true'
            if (pregnancies <= 9):
                return u'false'
