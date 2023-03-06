import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import MealMenu
import Menu
import Tuples
from Anaekran_UI import *
from Objects import *
from siparis_gecmisi import *
from PyQt5.QtCore import Qt

class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.pizza_ad_cheB()
        # self.veri_ekle({'pizza': 'margarita Pizza', 'malzeme': 'zeytin, et, mantar', 'fiyat': 87})
        MealMenu.pizza_menu(self)
        MealMenu.ingredient_menu(self)
        MealMenu.sauce_menu(self)
        MealMenu.drink_menu(self)
        self.ui.sepete_ekle_button.clicked.connect(self.sepete_ekle)
        self.ui.klas_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.Mar_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.turk_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.s_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.ketcap_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.mayonez_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.hardal_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.bbq_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.aci_sos_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.ranch_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.kola_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.fanta_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.gazoz_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.limonata_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.ayran_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.ketcap_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.mayonez_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.hardal_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.bbq_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.aci_sos_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.ranch_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.kola_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.fanta_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.gazoz_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.limonata_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.ayran_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.Auto_increament_spinbox()
        self.sipari_gecmisi= Siparis_Gecmisi()
        self.ui.actionGe_mi_Sipari_lerim.triggered.connect(self.siparis_gecmis_ac)
        #self.ui.ketcap_check.stateChanged.connect(self.a)
        self.siparis = []




    def siparis_gecmis_ac(self):
        self.sipari_gecmisi.show()

    def sepete_ekle(self):
        self.pizza_secim(Tuples.pizza_tuple(self))
        self.malzeme_secimi(Tuples.ingredient_tuple(self))
        self.sos_secim(Tuples.sauce_tuple(self))
        self.icecekler_secim(Tuples.drinks_tuple(self))
        a = self.sozluk_olustur(self.siparis)
        self.tabloya_veri_ekle(a)
        return a

    def pizza_secim(self, pizza_listesi):
        for eleman in pizza_listesi:
            if eleman[2] == True:
                self.siparis.append(eleman[0:2])
        return self.siparis

    def malzeme_secimi(self, malzeme_listesi):
        for eleman in malzeme_listesi:
            if eleman[2] == True:
                self.siparis.append(eleman[0:2])
        return self.siparis

    def sos_secim(self, sos_listesi):
        for i in sos_listesi:
            if i[2] == True:
                self.siparis.append(i[0:2])
        return self.siparis

    def icecekler_secim(self, icecek_listesi):
        for i in icecek_listesi:
            if i[2] == True:
                self.siparis.append(i[0:2])
        return self.siparis

    #def a(self):
        #self.ui.spinBox_aci_sos_4.setValue(self..value()+1)

    def sozluk_olustur(self, siparis_listesi):

        pizzalar = [classic.get_description(),
                 margherita.get_description(),
                 turk.get_description(), 
                 dominos.get_description()]
        
    
        malzemeler = [olive.get_description(),
                 mushroom.get_description(),
                 goat_cheese.get_description(),
                 meat.get_description(),
                 onion.get_description(),
                 corn.get_description()]
    

        soslar =  [ketchup.get_description(), 
                mayo.get_description(),
                mustard.get_description(), 
                bbq.get_description(),
                hot_sauce.get_description(),
                ranch.get_description()]
    

        icecekler = [coke.get_description(), 
                 fanta.get_description(),
                 pop_soda.get_description(),
                 lemonade.get_description(),
                 ayran.get_description()]

        sepet_ekle = {"Pizza": "", "Malzemeler": "", "Soslar": "", "İçecekler": "", "Fiyat": 0, "Notlar": ""}
        for veri in siparis_listesi:
            if veri[0] in pizzalar :
                sepet_ekle['Pizza'] = veri[0]
            elif  veri[0] in soslar:
                if sepet_ekle["Soslar"] != "":
                    sepet_ekle["Soslar"] += ", "
                sepet_ekle["Soslar"] += veri[0]
            elif  veri[0] in icecekler:
                if sepet_ekle["İçecekler"] != "":
                    sepet_ekle["İçecekler"] += ", "
                sepet_ekle["İçecekler"] += veri[0]
            else:
                if sepet_ekle["Malzemeler"] != "":
                    sepet_ekle["Malzemeler"] += ", "
                sepet_ekle["Malzemeler"] += veri[0]
            sepet_ekle["Fiyat"] += veri[1]
            sepet_ekle["Notlar"] = self.ui.plainTextEdit.toPlainText()
        return sepet_ekle
        
        #self.ui.plainTextEdit.text()

        

    def checkBox_secim(self):
        check_box = [
            [self.ui.klas_pizza_check, self.ui.klas_pizza_check.isChecked()],
            [self.ui.Mar_pizza_check, self.ui.Mar_pizza_check.isChecked()],
            [self.ui.turk_pizza_check, self.ui.turk_pizza_check.isChecked()],
            [self.ui.s_pizza_check, self.ui.s_pizza_check.isChecked()]
        ]

        for checkbox in check_box:
            if checkbox[1]:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(False)
                        self.siparis.clear()
                checkbox[1] = False
                break
            else:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(True)
                    self.siparis.clear()

    def soslar_icecekler_check(self):
            check_box_soslar_icecekler = [
                [self.ui.ketcap_check, self.ui.ketcap_check.isChecked()],
                [self.ui.mayonez_check, self.ui.mayonez_check.isChecked()],
                [self.ui.hardal_check, self.ui.hardal_check.isChecked()],
                [self.ui.bbq_check, self.ui.bbq_check.isChecked()],
                [self.ui.aci_sos_check, self.ui.aci_sos_check.isChecked()],
                [self.ui.ranch_check, self.ui.ranch_check.isChecked()],
                [self.ui.kola_check, self.ui.kola_check.isChecked()],
                [self.ui.fanta_check, self.ui.fanta_check.isChecked()],
                [self.ui.gazoz_check, self.ui.gazoz_check.isChecked()],
                [self.ui.limonata_check, self.ui.limonata_check.isChecked()],
                [self.ui.ayran_check, self.ui.ayran_check.isChecked()]
            ]
            for checkbox in check_box_soslar_icecekler:
                if checkbox[1]:
                    for other_checkbox in check_box_soslar_icecekler:
                        if other_checkbox[0] != checkbox[0]:
                            self.siparis.clear()
                    checkbox[1] = False
                    break
                else:
                    for other_checkbox in check_box_soslar_icecekler:
                        if other_checkbox[0] != checkbox[0]:
                            self.siparis.clear()

    def Auto_increament_spinbox(self):
        checkBox = [self.ui.ketcap_check,
                        self.ui.mayonez_check,
                        self.ui.hardal_check,
                        self.ui.bbq_check,
                        self.ui.aci_sos_check,
                        self.ui.ranch_check, 
                        self.ui.kola_check,
                        self.ui.fanta_check,
                        self.ui.gazoz_check,
                        self.ui.limonata_check,
                        self.ui.ayran_check
                          ]
        spinBox= [self.ui.spinBox_ketcap_4,
                        self.ui.spinBox_mayonez_4,
                        self.ui.spinBox_hardal_4,
                        self.ui.spinBox_bbq_4,
                        self.ui.spinBox_aci_sos_4,
                        self.ui.spinBox_ranch_4, 
                        self.ui.spinBox_KOLA,
                        self.ui.spinBox_FANTA,
                        self.ui.spinBox_GAZOZ,
                        self.ui.spinBox_LMONATA,
                        self.ui.spinBox_AYRAN]
      
        for i, e in enumerate(checkBox):
            if e.isChecked():
                spinBox[i].setValue(1)
            else:
                # checkbox false konumuna geldiğinde spinbox değerini 0 yap
                spinBox[i].setValue(0)


    def tabloya_veri_ekle(self, veriler):
        table_widget = self.ui.sepet_table
        row_count = table_widget.rowCount()
        table_widget.setRowCount(row_count + 1)
        row = row_count

        # yeni bir QTableWidgetItem objesi oluştur
        pizza_item = QTableWidgetItem(veriler["Pizza"])
        malzeme_item = QTableWidgetItem(veriler["Malzemeler"])
        sos_item = QTableWidgetItem(veriler["Soslar"])
        icecekler_item = QTableWidgetItem(veriler["İçecekler"])
        tutar_item = QTableWidgetItem(str(veriler["Fiyat"]))
        notlar_item = QTableWidgetItem(veriler["Notlar"])

        # Tablonun dışarıdan erişilmesini engelleme
        pizza_item.setFlags(pizza_item.flags() ^ Qt.ItemIsEditable)
        malzeme_item.setFlags(malzeme_item.flags() ^ Qt.ItemIsEditable)
        sos_item.setFlags(sos_item.flags() ^ Qt.ItemIsEditable)
        icecekler_item.setFlags(icecekler_item.flags() ^ Qt.ItemIsEditable)
        tutar_item.setFlags(tutar_item.flags() ^ Qt.ItemIsEditable)
        notlar_item.setFlags(notlar_item.flags() ^ Qt.ItemIsEditable)

        # QTableWidgetItem objelerini tableWidget'a ekle
        table_widget.setItem(row, 0, pizza_item)
        table_widget.setItem(row, 1, malzeme_item)
        table_widget.setItem(row, 2, sos_item)
        table_widget.setItem(row, 3, icecekler_item)
        table_widget.setItem(row, 4, tutar_item)
        table_widget.setItem(row, 5, notlar_item)

        #  Sil Sütununa Checkbox eklenmesi
        checkbox_item = QTableWidgetItem()
        checkbox_item.setCheckState(Qt.Checked)
        table_widget.setItem(row, 6, checkbox_item)




uyg = QApplication(sys.argv)
pencere = MainPage()
pencere.show()
sys.exit(uyg.exec_())

