style = '''
QWidget {

     font: medium Ubuntu;
     font-size: 16px;
     background-image: url("pictures/background.jpg")
}
QPushButton {                                      
    background: #B16CED;
    border: 1px solid black;
    border-radius: 5px;
    border-width: 1px;
    font: bold 14px;
}
QPushButton:hover {
    border: 1px solid black;
    border-radius: 5px;
    border-width: 1px;
    background: #CB9BF6; 
    color: white;
} 
QPushButton:pressed {  
     border: 1px solid black;
     border-radius: 5px;
     border-width: 1px;                   
     background: #D9A8FC;
     color: #f6f6f6;
    }
QComboBox{
     border: 1px solid black;
     border-radius: 2px;
     padding: 1px 18px 1px 3px;
     min-width: 6em;
}
QComboBox:editable {
     background:#E6E6FA;
}
QComboBox:!editable, QComboBox::drop-down:editable {
      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #E6E6FA, stop: 0.4 #DDDDDD,
                                  stop: 0.5 #D8D8D8, stop: 1.0 #D9A8FC);
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #D9A8FC, stop: 0.4 #E6E6FA,
                                 stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}
QComboBox:on {
     padding-top: 3px;
     padding-left: 4px;
}
QComboBox QAbstractItemView {
     font: Arial;
     font-size: 16px;
     border: 2px solid black;
     selection-background-color:gray;
     background:#E6E6FA; 
}

QLabel {
    background: #D9A8FC;
    font: Arial;
    font-size: 18px;
    color:#000000;   
    qproperty-alignment: AlignCenter;


}      
QTextEdit
{
   background:#E6E6FA;
   font: Arial;
   font-size: 22px;
   border: 1px solid black;
   border-radius: 5px;
   border-width: 2px;
}
QMessageBox
{
   background:#D9A8FC;
   font: Arial;
   font-size: 16px;
}


'''