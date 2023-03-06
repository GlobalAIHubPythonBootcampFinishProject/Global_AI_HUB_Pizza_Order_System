import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import Menu
from Anaekran_UI import *
from siparis_gecmisi import *
from PyQt5.QtCore import Qt
from Product.Ingredient.SubIngredient import Olive, Mushroom, GoatCheese, Meat, Onion, Corn
from Product.Pizza.SubPizza import Classic, Turk, Margherita, Dominos
from Product.Sauce.SubSauce import Mayo, Mustard, Ketchup, BBQ, Hot, Ranch
from Product.Drink.SubDrink import Coke, Ayran, OrangeJuice, SodaPop,Lemonade

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.pizza_ad_cheB()
        # self.veri_ekle({'pizza': 'margarita Pizza', 'malzeme': 'zeytin, et, mantar', 'fiyat': 87})
        self.pizza_menu()
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
        self.pizza_secim(self.pizza_tuple())
        self.malzeme_secimi(self.ingredient_tuple())
        self.sos_secim(self.soslar_tuple())
        self.icecekler_secim(self.icecekler_tuple())
        self.sozluk_olustur(self.siparis)

        return print(self.siparis)

    def pizza_tuple(self):
        dominos = Dominos("Domino's pizza plain", Menu.Costs.dominos_pizza_cost())
        turk = Turk("Turkish style pizza plain", Menu.Costs.turk_pizza_cost())
        margherita = Margherita("Margherita pizza plain", Menu.Costs.margarita_pizza_cost())
        classic = Classic("Classic pizza plain", Menu.Costs.klasik_pizza_cost())
        pizzalar_tuple = [
            (classic.get_description(), classic.get_cost(), self.ui.klas_pizza_check.isChecked()),
            (margherita.get_description(), margherita.get_cost(), self.ui.Mar_pizza_check.isChecked()),
            (turk.get_description(), turk.get_cost(), self.ui.turk_pizza_check.isChecked()),
            (dominos.get_description(), dominos.get_cost(), self.ui.s_pizza_check.isChecked())
        ]
        return pizzalar_tuple

    def ingredient_tuple(self):
        olive = Olive("Zeytin", Menu.Costs.zeytin_cost())
        mushroom = Mushroom("Mantar", Menu.Costs.mantar_cost())
        goat_cheese = GoatCheese("Keçi Peyniri", Menu.Costs.keci_peyniri_cost())
        meat = Meat("Et", Menu.Costs.et_cost())
        onion = Onion("Sogan", Menu.Costs.sogan_cost())
        corn = Corn("Misir", Menu.Costs.misir_cost())

        ingredient_tuple = [
            (olive.get_description(), olive.get_cost(), self.ui.zeytin_check.isChecked()),
            (mushroom.get_description(), mushroom.get_cost(), self.ui.mantar_check.isChecked()),
            (goat_cheese.get_description(), goat_cheese.get_cost(), self.ui.keci_peyniri_check.isChecked()),
            (meat.get_description(), meat.get_cost(), self.ui.et_check.isChecked()),
            (onion.get_description(), onion.get_cost(), self.ui.sogan_check.isChecked()),
            (corn.get_description(), corn.get_cost(), self.ui.misir_check.isChecked())
        ]
        return ingredient_tuple

    def soslar_tuple(self):
        ketcap = Ketchup("Ketçap", Menu.Costs.ketcap_cost())
        mayonez = Mayo("Mayonez", Menu.Costs.mayonez_cost())
        hardal = Mustard("Hardal", Menu.Costs.hardal_cost())
        bbq = BBQ("BBQ Sos", Menu.Costs.bbq_cost())
        aci_sos = Hot("Acı Sos", Menu.Costs.aci_sos_cost())
        ranch_sos = Ranch("Ranch Sos", Menu.Costs.ranch_cost())

        soslar_tuple = [(ketcap.get_description(), ketcap.get_cost()*self.ui.spinBox_ketcap_4.value(), self.ui.ketcap_check.isChecked()),
                        (mayonez.get_description(), mayonez.get_cost()*self.ui.spinBox_mayonez_4.value() , self.ui.mayonez_check.isChecked()),
                        (hardal.get_description(), hardal.get_cost()*self.ui.spinBox_hardal_4.value() , self.ui.hardal_check.isChecked()),
                        (bbq.get_description(), bbq.get_cost()*self.ui.spinBox_bbq_4.value() , self.ui.bbq_check.isChecked()),
                        (aci_sos.get_description(), aci_sos.get_cost()*self.ui.spinBox_aci_sos_4.value() , self.ui.aci_sos_check.isChecked()),
                        (ranch_sos.get_description(), ranch_sos.get_cost()*self.ui.spinBox_ranch_4.value() , self.ui.ranch_check.isChecked())
                        ]
        return soslar_tuple

    def icecekler_tuple(self):
        kola = Coke("Kola", Menu.Costs.kola_cost())
        fanta = OrangeJuice("Fanta", Menu.Costs.fanta_cost())
        gazoz = SodaPop("Gazoz", Menu.Costs.gazoz_cost())
        limonata = Lemonade("Limonata", Menu.Costs.limonata_cost())
        ayran = Ayran("Ayran", Menu.Costs.ayran_cost())

        icecekler_tuple = [(kola.get_description(), kola.get_cost()*self.ui.spinBox_KOLA.value(), self.ui.kola_check.isChecked()),
                           (fanta.get_description(), fanta.get_cost()*self.ui.spinBox_FANTA.value(), self.ui.fanta_check.isChecked()),
                           (gazoz.get_description(), gazoz.get_cost()*self.ui.spinBox_GAZOZ.value(), self.ui.gazoz_check.isChecked()),
                           (limonata.get_description(), limonata.get_cost()*self.ui.spinBox_LMONATA.value(), self.ui.limonata_check.isChecked()),
                           (ayran.get_description(), ayran.get_cost()*self.ui.spinBox_AYRAN.value(), self.ui.ayran_check.isChecked())]
        
        return icecekler_tuple
    
   
    
   

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

    def sozluk_olustur(self,siparis_listesi):
         
        dominos = Dominos("Domino's pizza plain", Menu.Costs.dominos_pizza_cost())
        turk = Turk("Turkish style pizza plain", Menu.Costs.turk_pizza_cost())
        margherita = Margherita("Margherita pizza plain", Menu.Costs.margarita_pizza_cost())
        classic = Classic("Classic pizza plain", Menu.Costs.klasik_pizza_cost())
        
        pizzalar = [classic.get_description(),
                 margherita.get_description(),
                 turk.get_description(),
                 dominos.get_description()]
    

        olive = Olive("Zeytin", Menu.Costs.zeytin_cost())
        mushroom = Mushroom("Mantar", Menu.Costs.mantar_cost())
        goat_cheese = GoatCheese("Keçi Peyniri", Menu.Costs.keci_peyniri_cost())
        meat = Meat("Et", Menu.Costs.et_cost())
        onion = Onion("Sogan", Menu.Costs.sogan_cost())
        corn = Corn("Misir", Menu.Costs.misir_cost())
    
        malzemeler = [olive.get_description(),
                     mushroom.get_description(),
                     goat_cheese.get_description(),
                     meat.get_description(),
                     onion.get_description(),
                     corn.get_description()]
    
        ketcap = Ketchup("Ketçap", Menu.Costs.ketcap_cost())
        mayonez = Mayo("Mayonez", Menu.Costs.mayonez_cost())
        hardal = Mustard("Hardal", Menu.Costs.hardal_cost())
        bbq = BBQ("BBQ Sos", Menu.Costs.bbq_cost())
        aci_sos = Hot("Acı Sos", Menu.Costs.aci_sos_cost())
        ranch_sos = Ranch("Ranch Sos", Menu.Costs.ranch_cost())

        soslar = [ketcap.get_description(), 
                  mayonez.get_description(),
                  hardal.get_description(), 
                  bbq.get_description(),
                  aci_sos.get_description(),
                  ranch_sos.get_description()]
        
        kola = Coke("Kola", Menu.Costs.kola_cost())
        fanta = OrangeJuice("Fanta", Menu.Costs.fanta_cost())
        gazoz = SodaPop("Gazoz", Menu.Costs.gazoz_cost())
        limonata = Lemonade("Limonata", Menu.Costs.limonata_cost())
        ayran = Ayran("Ayran", Menu.Costs.ayran_cost())

        icecekler = [kola.get_description(), 
                    fanta.get_description(),
                    gazoz.get_description(),
                    limonata.get_description(),
                    ayran.get_description()]
                        

        
        sepet_ekle = {"Pizza": "", "Malzemeler": "", "Soslar": "", "İçecekler": "", "Fiyat": 0, "Notlar": ""}
        for veri in siparis_listesi:
            if veri[0] in pizzalar :
                sepet_ekle['Pizza'] = veri[0]
            elif "Sos" in veri[0]:
                if sepet_ekle["Soslar"] != "":
                    sepet_ekle["Soslar"] += ", "
                sepet_ekle["Soslar"] += veri[0]
            elif "İçecek" in veri[0]:
                if sepet_ekle["İçecekler"] != "":
                    sepet_ekle["İçecekler"] += ", "
                sepet_ekle["İçecekler"] += veri[0]
            else:
                if sepet_ekle["Malzemeler"] != "":
                    sepet_ekle["Malzemeler"] += ", "
                sepet_ekle["Malzemeler"] += veri[0]
            sepet_ekle["Fiyat"] += veri[1]
            sepet_ekle["Notlar"] = ""
        return print (sepet_ekle)
        
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
      
        for i,e in enumerate(checkBox):
            if  e.isChecked():
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

    def pizza_menu(self):
        dominos = Dominos("Sade pizza", Menu.Costs.dominos_pizza_cost())
        turk = Turk("Türk Pizza", Menu.Costs.turk_pizza_cost())
        margherita = Margherita("Margherita Pizza", Menu.Costs.margarita_pizza_cost())
        classic = Classic("Klasik Pizza", Menu.Costs.klasik_pizza_cost())

        menu= (
        f"1. {classic.get_description()}          -----> {classic.get_cost()} $" + "\n" + 
        f"2. {margherita.get_description()} -----> {margherita.get_cost()} $" + "\n" + 
        f"3. {turk.get_description()}            -----> {turk.get_cost()} $" + "\n" + 
        f"4. {dominos.get_description()}           -----> {dominos.get_cost()} $")

        self.ui.pizza_menu.setText(menu)


uyg = QApplication(sys.argv)
pencere = MainPage()
pencere.show()
sys.exit(uyg.exec_())

