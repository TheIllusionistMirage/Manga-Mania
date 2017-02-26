#!/usr/bin/python3

'''

    Manga-Mania
    ------------
    
    Author: Koushtav Chakrabarty <TheIllusionistMirage>
    Email:  koushtav at fleptic dot eu
    
    The GUI module decouples the UI portion of Manga-Mania.
    It subclasses several PyQt5 classes in order to provice
    an enhanced, customized functionality.
    
    This code is licensed under the MIT license. Please see
    `LICENSE` file for more info.

'''


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class GUI(QMainWindow):

    '''
    
    Class GUI provides the UI part of Manga-Mania. An
    instance of the `GUI` class should be used to handle
    all GUI related activities.
    
    '''
    
    def __init__(self):
        
        '''
        
        Default constructor
        
        '''
        
        super().__init__()
        self.initializeUI()
        
        
    def initializeUI(self):
    
        # Base URL for search
        self.sURL = 'http://mangafox.me/search.php?'

        # Search method
        # (cw = contain, bw = begin, ew = end)
        self.sNAME_METHOD = 'name_method=cw'

        # Search key (text, max. 150 chars)
        self.sNAME = '&name='

        # Search type
        # (0 = Any, 1 = Japanese Manga, 2 = Korean Manhwa, 3 = Chinese Manhua)
        self.sTYPE = '&type=0'

        # Author method
        # (cw = contain, bw = begin, ew = end)
        self.sAUTHOR_METHOD = '&author_method=cw'

        # Author name (text, max. 50 chars)
        self.sAUTHOR = '&author='

        # Artist method
        # (cw = contain, bw = begin, ew = end)
        self.sARTIST_METHOD = '&artist_method=cw'

        # Artist name (text, max. 50 chars)
        self.sARTIST = '&artist='

        # Genres
        # (0 = default, 1 = include, 2 = exclude)
        self.sGENRE_ACTION        = '&genres%5BAction%5D=0'
        self.sGENRE_ADULT         = '&genres%5BAdult%5D=0'
        self.sGENRE_ADVENTURE     = '&genres%5BAdventure%5D=0'
        self.sGENRE_COMEDY        = '&genres%5BComedy%5D=0'
        self.sGENRE_DOUJINSHI     = '&genres%5BDoujinshi%5D=0'
        self.sGENRE_DRAMA         = '&genres%5BDrama%5D=0'
        self.sGENRE_ECCHI         = '&genres%5BEcchi%5D=0'
        self.sGENRE_FANTASY       = '&genres%5BFantasy%5D=0'
        self.sGENRE_GENDER_BENDER = '&genres%5BGender+Bender%5D=0'
        self.sGENRE_HAREM         = '&genres%5BHarem%5D=0'
        self.sGENRE_HISTORICAL    = '&genres%5BHistorical%5D=0'
        self.sGENRE_HORROR        = '&genres%5BHorror%5D=0'
        self.sGENRE_JOSEI         = '&genres%5BJosei%5D=0'
        self.sGENRE_MARTIAL_ARTS   = '&genres%5BMartial+Arts%5D=0'
        self.sGENRE_MATURE        = '&genres%5BMature%5D=0'
        self.sGENRE_MECHA         = '&genres%5BMecha%5D=0'
        self.sGENRE_MYSTERY       = '&genres%5BMystery%5D=0'
        self.sGENRE_ONE_SHOT      = '&genres%5BOne+Shot%5D=0'
        self.sGENRE_PSYCHOLOGICAL = '&genres%5BPsychological%5D=0'
        self.sGENRE_ROMANCE       = '&genres%5BRomance%5D=0'
        self.sGENRE_SCHOOL_LIFE   = '&genres%5BSchool+Life%5D=0'
        self.sGENRE_SCI_FI        = '&genres%5BSci-fi%5D=0'
        self.sGENRE_SEINEN        = '&genres%5BSeinen%5D=0'
        self.sGENRE_SHOUJO        = '&genres%5BShoujo%5D=0'
        self.sGENRE_SHOUJO_AI     = '&genres%5BShoujo+Ai%5D=0'
        self.sGENRE_SHOUNEN       = '&genres%5BShounen%5D=0'
        self.sGENRE_SHOUNEN_AI    = '&genres%5BShounen+Ai%5D=0'
        self.sGENRE_SLICE_OF_LIFE = '&genres%5BSlice+of+Life%5D=0'
        self.sGENRE_SMUT          = '&genres%5BSmut%5D=0'
        self.sGENRE_SPORTS        = '&genres%5BSports%5D=0'
        self.sGENRE_SUPERNATURAL  = '&genres%5BSupernatural%5D=0'
        self.sGENRE_TRAGEDY       = '&genres%5BTragedy%5D=0'
        self.sGENRE_WEBTOONS      = '&genres%5BWebtoons%5D=0'
        self.sGENRE_YAOI          = '&genres%5BYaoi%5D=0'
        self.sGENRE_YURI          = '&genres%5BYuri%5D=0'

        # Release method
        # (eq = On, before = lt, after = gt)
        self.sRELEASE_METHOD = '&released_method=eq'

        # Relase data (YYYY)
        self.sRELEASE_DATE = '&released='

        # Rating method
        # (eq = Equal, lt = Less Than, gt = Greater Than)
        self.sRATING_METHOD = '&rating_method=eq'

        # Rating (0-5 stars)
        # (0 to 5 = zero to five stars)
        # Leave blank if rating is not required
        self.sRATING = '&rating='

        # Series running or completed
        # (0 = No, 1 = Yes)
        # Leave blank if running info is not required
        self.sRUNNING = '&is_completed='

        # Set advanced search options ON
        self.sADVANCED_OPTIONS = '&advopts=1i'
    
            
        # Add status bar
        self.statusBar().showMessage('Ready')

        # Set initial geometry
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('MangaFox Search Scraper')
        self.show()

        # Search action
        searchAction = QAction(QIcon('resources/images/search-icon.png'), '&Search', self)
        searchAction.setShortcut('Ctrl+S')
        searchAction.setStatusTip('Search the MangaFox database')
        searchAction.triggered.connect(self.searchMFDB)

        # Exit action
        exitAction = QAction(QIcon('resources/images/exit-icon.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+X')
        exitAction.setStatusTip('Exit the application')
        exitAction.triggered.connect(qApp.quit)

        # About action
        aboutAction = QAction(QIcon('resources/images/about-icon.png'), '&About', self)
        aboutAction.setStatusTip('Show brief application info')
        aboutAction.triggered.connect(self.aboutInfo)

        # Add menubar
        menubar = self.menuBar()
        
        # File menu
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(searchAction)
        fileMenu.addAction(exitAction)

        # About menu
        aboutMenu = menubar.addMenu('&About')
        #aboutMenu.addAction(helpAction)
        aboutMenu.addAction(aboutAction)


    def searchMFDB(self):

        print('Search initiated')
        self.searchDialog()


    def aboutInfo(self):

        dialog = QDialog(self)
        dialog.setWindowTitle('About MangaFox Search Scraper')
        dialog.resize(400, 200)
        dialog.setModal(False)
        dialog.exec_() # dialog.exec_()
    

    def searchDialog(self):

        self.sd = QDialog(self)
        self.sd.setWindowTitle('Search MangaFox database')
        self.sd.resize(610, 570)

        self.searchLabel = QLabel(self.sd)
        self.searchLabel.setText('<b>Search:</b>')
        self.searchLabel.move(20,  20)
        self.searchLabel.adjustSize()

        self.searchBox = QLineEdit(self.sd)
        self.searchBox.setText('')
        self.searchBox.setMaxLength(150)
        self.searchBox.resize(200, 20)
        self.searchBox.move(90, 18)
        #self.searchBox.textChanged[str].connect(self.updateName)

        self.scw = QRadioButton('Contain', self.sd)
        self.scw.move(350, 18)
        
        self.sbw = QRadioButton('Begin', self.sd)
        self.sbw.move(440, 18)
        
        self.sew = QRadioButton('End', self.sd)
        self.sew.move(520, 18)
        
        self.sbg = QButtonGroup(self.sd)
        self.sbg.addButton(self.scw)
        self.sbg.addButton(self.sbw)
        self.sbg.addButton(self.sew)
        self.sbg.setExclusive(True)
        #self.sbg.clicked.connect(self.updateNameMethod)
        self.scw.toggle()
        
        # Select the type of manga

        self.typeLabel = QLabel('<b>Type:</b>', self.sd)
        self.typeLabel.move(20, 62)

        self.tjp = QRadioButton('Japanese Manga', self.sd)
        self.tjp.move(80, 60)

        self.tkr = QRadioButton('Korean Manhwa', self.sd)
        self.tkr.move(230, 60)

        self.tch = QRadioButton('Chinese Manhua', self.sd)
        self.tch.move(370, 60)

        self.tan  = QRadioButton('Any', self.sd)
        self.tan.move(520, 60)

        self.tbg = QButtonGroup(self.sd)
        self.tbg.addButton(self.tjp)
        self.tbg.addButton(self.tkr)
        self.tbg.addButton(self.tch)
        self.tbg.addButton(self.tan)
        self.tbg.setExclusive(True)
        self.tan.toggle()

        # Author name
        
        self.authorLabel = QLabel('<b>Author Name:</b>', self.sd)
        self.authorLabel.move(20, 102)

        self.authorBox = QLineEdit('', self.sd)
        self.authorBox.setMaxLength(50)
        self.authorBox.resize(200, 20)
        self.authorBox.move(130, 100)

        self.aucw = QRadioButton('Contain', self.sd)
        self.aucw.move(350, 100)
        
        self.aubw = QRadioButton('Begin', self.sd)
        self.aubw.move(440, 100)
        
        self.auew = QRadioButton('End', self.sd)
        self.auew.move(520, 100)
        
        self.aubg = QButtonGroup(self.sd)
        self.aubg.addButton(self.aucw)
        self.aubg.addButton(self.aubw)
        self.aubg.addButton(self.auew)
        self.aubg.setExclusive(True)
        self.aucw.toggle()

        # Artist name

        self.artistLabel = QLabel('<b>Artist Name:</b>', self.sd)
        self.artistLabel.move(20, 142)

        self.artistBox = QLineEdit('', self.sd)
        self.artistBox.setMaxLength(50)
        self.artistBox.resize(200, 20)
        self.artistBox.move(130, 140)

        self.arcw = QRadioButton('Contain', self.sd)
        self.arcw.move(350, 140)
        
        self.arbw = QRadioButton('Begin', self.sd)
        self.arbw.move(440, 140)
        
        self.arew = QRadioButton('End', self.sd)
        self.arew.move(520, 140)
        
        self.arbg = QButtonGroup(self.sd)
        self.arbg.addButton(self.arcw)
        self.arbg.addButton(self.arbw)
        self.arbg.addButton(self.arew)
        self.arbg.setExclusive(True)
        self.arcw.toggle()

        # Genre

        self.genreLabel =QLabel('<b>Genre</b> (single click to select, double click to exclude):', self.sd)
        self.genreLabel.move(20, 192)

        self.gaction = QCheckBox('Action', self.sd)
        self.gaction.move(20, 220)

        self.gadult = QCheckBox('Adult', self.sd)
        self.gadult.move(140, 220)

        self.gadventure = QCheckBox('Adventure', self.sd)
        self.gadventure.move(260, 220)

        self.gcomedy = QCheckBox('Comedy', self.sd)
        self.gcomedy.move(380, 220)

        self.gdoujinshi = QCheckBox('Doujinshi', self.sd)
        self.gdoujinshi.move(500, 220)

        self.gdrama = QCheckBox('Drama', self.sd)
        self.gdrama.move(20, 240)

        self.gecchi = QCheckBox('Ecchi', self.sd)
        self.gecchi.move(140, 240)

        self.gfantasy = QCheckBox('Fantasy', self.sd)
        self.gfantasy.move(260, 240)

        self.ggenben = QCheckBox('Gender Bender', self.sd)
        self.ggenben.move(380, 240)

        self.gharem = QCheckBox('Harem', self.sd)
        self.gharem.move(500, 240)

        self.ghistorical = QCheckBox('Historical', self.sd)
        self.ghistorical.move(20, 260)

        self.ghorror = QCheckBox('Horror', self.sd)
        self.ghorror.move(140, 260)

        self.gjosei = QCheckBox('Josei', self.sd)
        self.gjosei.move(260, 260)

        self.gmartart = QCheckBox('Martial Arts', self.sd)
        self.gmartart.move(380, 260)

        self.gmature = QCheckBox('Mature', self.sd)
        self.gmature.move(500, 260)

        self.gmecha = QCheckBox('Mecha', self.sd)
        self.gmecha.move(20, 280)

        self.gmystery = QCheckBox('Mystery', self.sd)
        self.gmystery.move(140, 280)

        self.gones = QCheckBox('One Shot', self.sd)
        self.gones.move(260, 280)

        self.gpsych = QCheckBox('Psychological', self.sd)
        self.gpsych.move(380, 280)

        self.gromance = QCheckBox('Romance', self.sd)
        self.gromance.move(500, 280)

        self.gschlyf = QCheckBox('School Life', self.sd)
        self.gschlyf.move(20, 300)

        self.gscifi = QCheckBox('Sci-fi', self.sd)
        self.gscifi.move(140, 300)

        self.gseinen = QCheckBox('Seinen', self.sd)
        self.gseinen.move(260, 300)

        self.gshoujo = QCheckBox('Shoujo', self.sd)
        self.gshoujo.move(380, 300)

        self.gshoujoai = QCheckBox('Shoujo Ai', self.sd)
        self.gshoujoai.move(500, 300)

        self.gshou = QCheckBox('Shounen', self.sd)
        self.gshou.move(20, 320)

        self.gshouai = QCheckBox('Shounen Ai', self.sd)
        self.gshouai.move(140, 320)

        self.gslice = QCheckBox('Slice of Life', self.sd)
        self.gslice.move(260, 320)

        self.gsmut = QCheckBox('Smut', self.sd)
        self.gsmut.move(380, 320)

        self.gsports = QCheckBox('Sports', self.sd)
        self.gsports.move(500, 320)
        
        self.gsuper = QCheckBox('Supernatural', self.sd)
        self.gsuper.move(20, 340)

        self.gtrag = QCheckBox('Tragedy', self.sd)
        self.gtrag.move(140, 340)

        self.gwtoons = QCheckBox('Webtoons', self.sd)
        self.gwtoons.move(260, 340)

        self.gyaoi = QCheckBox('Yaoi', self.sd)
        self.gyaoi.move(380, 340)

        self.gyuri = QCheckBox('Yuri', self.sd)
        self.gyuri.move(500, 340)

        self.gbg = QButtonGroup(self.sd)
        self.gbg.addButton(self.gaction)
        self.gbg.addButton(self.gadult)
        self.gbg.addButton(self.gadventure)
        self.gbg.addButton(self.gcomedy)
        self.gbg.addButton(self.gdoujinshi)
        self.gbg.addButton(self.gdrama)
        self.gbg.addButton(self.gecchi)
        self.gbg.addButton(self.gfantasy)
        self.gbg.addButton(self.ggenben)
        self.gbg.addButton(self.gharem)
        self.gbg.addButton(self.ghistorical)
        self.gbg.addButton(self.ghorror)
        self.gbg.addButton(self.gjosei)
        self.gbg.addButton(self.gmartart)
        self.gbg.addButton(self.gmature)
        self.gbg.addButton(self.gmecha)
        self.gbg.addButton(self.gmystery)
        self.gbg.addButton(self.gones)
        self.gbg.addButton(self.gpsych)
        self.gbg.addButton(self.gromance)
        self.gbg.addButton(self.gschlyf)
        self.gbg.addButton(self.gscifi)
        self.gbg.addButton(self.gseinen)
        self.gbg.addButton(self.gshoujo)
        self.gbg.addButton(self.gshoujoai)
        self.gbg.addButton(self.gshou)
        self.gbg.addButton(self.gshouai)
        self.gbg.addButton(self.gslice)
        self.gbg.addButton(self.gsmut)
        self.gbg.addButton(self.gsports)
        self.gbg.addButton(self.gsuper)
        self.gbg.addButton(self.gtrag)
        self.gbg.addButton(self.gwtoons)
        self.gbg.addButton(self.gyaoi)
        self.gbg.addButton(self.gyuri)

        self.gbg.setExclusive(False)

        # Release Year

        self.yearLabel = QLabel('<b>Year of Release:</b>', self.sd)
        self.yearLabel.move(20, 382)

        self.yearBox = QLineEdit('', self.sd)
        self.yearBox.setMaxLength(4)
        self.yearBox.resize(50, 20)
        self.yearBox.move(150, 380)

        self.yon = QRadioButton('On', self.sd)
        self.yon.move(220, 380)
        
        self.ybf = QRadioButton('Before', self.sd)
        self.ybf.move(290, 380)
        
        self.yaf = QRadioButton('After', self.sd)
        self.yaf.move(380, 380)
        
        self.ybg = QButtonGroup(self.sd)
        self.ybg.addButton(self.yon)
        self.ybg.addButton(self.ybf)
        self.ybg.addButton(self.yaf)
        self.ybg.setExclusive(True)
        self.yon.toggle()

        # Rating

        self.ratingLabel = QLabel('<b>Rating:</b>', self.sd)
        self.ratingLabel.move(20, 412)

        self.ris = QRadioButton('is', self.sd)
        self.ris.move(100, 410)

        self.rlt = QRadioButton('less than', self.sd)
        self.rlt.move(160, 410)

        self.rgt = QRadioButton('more than', self.sd)
        self.rgt.move(265, 410)

        self.rbg = QButtonGroup(self.sd)
        self.rbg.addButton(self.ris)
        self.rbg.addButton(self.rlt)
        self.rbg.addButton(self.rgt)
        self.rbg.setExclusive(True)
        self.ris.toggle()

        self.rany = QRadioButton('Any', self.sd)
        self.rany.move(20, 435)
        
        self.r0 = QRadioButton('0 stars', self.sd)
        self.r0.move(80, 435)

        self.r1 = QRadioButton('1 star', self.sd)
        self.r1.move(160, 435)

        self.r2 = QRadioButton('2 stars', self.sd)
        self.r2.move(240, 435)

        self.r3 = QRadioButton('3 stars', self.sd)
        self.r3.move(320, 435)

        self.r4 = QRadioButton('4 stars', self.sd)
        self.r4.move(400, 435)

        self.r5 = QRadioButton('5 stars', self.sd)
        self.r5.move(480, 435)

        self.rrbg = QButtonGroup(self.sd)
        self.rrbg.addButton(self.rany)
        self.rrbg.addButton(self.r0)
        self.rrbg.addButton(self.r1)
        self.rrbg.addButton(self.r2)
        self.rrbg.addButton(self.r3)
        self.rrbg.addButton(self.r4)
        self.rrbg.addButton(self.r5)
        self.rrbg.setExclusive(True)
        self.rany.toggle()

        # Series running

        self.runLabel = QLabel('<b>Completed Series:</b>', self.sd)
        self.runLabel.move(20, 477)

        self.ryes = QRadioButton('Yes', self.sd)
        self.ryes.move(170, 475)
        
        self.rno = QRadioButton('No', self.sd)
        self.rno.move(240, 475)
        
        self.ryn = QRadioButton('Either', self.sd)
        self.ryn.move(310, 475)

        self.cbg = QButtonGroup(self.sd)
        self.cbg.addButton(self.ryes)
        self.cbg.addButton(self.rno)
        self.cbg.addButton(self.ryn)
        self.cbg.setExclusive(True)
        self.ryn.toggle()

        # search button

        self.searchButton = QPushButton('Search', self.sd)
        self.searchButton.move(250, 520)
        #self.searchButton.clicked.connect(qApp.quit)
        self.searchButton.clicked.connect(self.searchMangaFox)

        # Draw the dialog
        self.sd.setModal(True)
        self.sd.exec_()


    def generateSearchURL(self):

        """
        
        Constructs the expected search URL with all query fields which is then fed to 
        `http://mangafox.me/search.php`

        """

        finalURL = (self.sURL + self.sNAME_METHOD + self.sNAME + self.sTYPE + self.sAUTHOR_METHOD + self.sAUTHOR + self.sARTIST_METHOD +
                   self.sARTIST + self.sGENRE_ACTION + self.sGENRE_ADULT + self.sGENRE_ADVENTURE + self.sGENRE_COMEDY + self.sGENRE_DOUJINSHI +
                   self.sGENRE_DRAMA + self.sGENRE_ECCHI + self.sGENRE_FANTASY + self.sGENRE_GENDER_BENDER + self.sGENRE_HAREM +
                   self.sGENRE_HISTORICAL + self.sGENRE_HORROR + self.sGENRE_JOSEI + self.sGENRE_MARTIAL_ARTS + self.sGENRE_MATURE +
                   self.sGENRE_MECHA + self.sGENRE_MYSTERY + self.sGENRE_ONE_SHOT + self.sGENRE_PSYCHOLOGICAL + self.sGENRE_ROMANCE +
                   self.sGENRE_SCHOOL_LIFE + self.sGENRE_SCI_FI + self.sGENRE_SEINEN + self.sGENRE_SHOUJO + self.sGENRE_SHOUJO_AI +
                   self.sGENRE_SHOUNEN + self.sGENRE_SHOUNEN_AI + self.sGENRE_SLICE_OF_LIFE + self.sGENRE_SMUT + self.sGENRE_SPORTS +
                   self.sGENRE_SUPERNATURAL + self.sGENRE_TRAGEDY + self.sGENRE_WEBTOONS + self.sGENRE_YAOI + self.sGENRE_YURI +
                   self.sRELEASE_METHOD + self.sRELEASE_DATE + self.sRATING_METHOD + self.sRATING + self.sRUNNING + self.sADVANCED_OPTIONS)
                   
        return finalURL


    def updateNameMethod(self):

        if self.scw.isChecked():            
            self.sNAME_METHOD = 'name_method=cw'

        elif self.sbw.isChecked():
            self.sNAME_METHOD = 'name_method=bw'

        else:
            self.sNAME_METHOD = 'name_method=ew'


    def updateName(self):

        self.sNAME = '&name=' + str(self.searchBox.text())
        
    
    def updateMangaType(self):
    
        if self.tjp.isChecked():
            self.sTYPE = '&type=1'
        
        elif self.tkr.isChecked():
            self.sTYPE = '&type=2'
            
        elif self.tch.isChecked():
            self.sTYPE = '&type=3'
        
        else:
            self.sTYPE = '&type=0'
            
    
    def updateAuthorMethod(self):
    
        if self.aucw.isChecked():
            self.sAUTHOR_METHOD = '&author_method=cw'
            
        elif self.aubw.isChecked():
            self.sAUTHOR_METHOD = '&author_method=bw'
        
        #elif self.auew.isChecked():
        else:
            self.sAUTHOR_METHOD = '&author_method=ew'
            
    
    def updateAuthor(self):
    
        self.sAUTHOR = '&author=' + str(self.authorBox.text())
        
    
    def updateArtistMethod(self):
    
        if self.arcw.isChecked():
            self.sARTIST_METHOD = '&artist_method=cw'
            
        elif self.arbw.isChecked():
            self.sARTIST_METHOD = '&artist_method=bw'
        
        #elif self.arew.isChecked():
        else:
            self.sARTIST_METHOD = '&artist_method=ew'
    
    
    def updateArtist(self):
    
        self.sARTIST = '&artist=' + str(self.artistBox.text())
    
    
    def updateGenres(self):
    
        #
        foo = 1
        
    
    def updateReleaseMethod(self):
    
        if self.yon.isChecked():
            self.sRELEASE_METHOD = '&released_method=eq'
        
        elif self.ybf.isChecked():
            self.sRELEASE_METHOD = '&released_method=lt'
            
        #elif self.yaf.isChecked():
        else:
            self.sRELEASE_METHOD = '&released_method=gt'
    
    
    def updateReleaseYear(self):
    
        self.sRELEASE_DATE = '&released=' + str(self.yearBox.text())
        
    
    def updateRatingMethod(self):
    
        if self.ris.isChecked():
            self.sRATING_METHOD = '&rating_method=eq'
        
        elif self.rlt.isChecked():
            self.sRATING_METHOD = '&rating_method=lt'
            
        #elif self.rgt.isChecked():
        else:
            self.sRATING_METHOD = '&rating_method=gt'
            
                        
    def updateRating(self):
    
        if self.r0.isChecked():
            self.sRATING = '&rating=0'
            
        elif self.r1.isChecked():
            self.sRATING = '&rating=1'
            
        elif self.r2.isChecked():
            self.sRATING = '&rating=2'
        
        elif self.r3.isChecked():
            self.sRATING = '&rating=3'
            
        elif self.r4.isChecked():
            self.sRATING = '&rating=4'
        
        elif self.r5.isChecked():
            self.sRATING = '&rating=5'
            
        #elif self.rany.isChecked():
        else:
            self.sRATING = '&rating='
            
            
    def isRunning(self):
    
        if self.ryes.isChecked():
            self.sRUNNING = '&is_completed=1'
        
        elif self.rno.isChecked():
            self.sRUNNING = '&is_completed=0'
        
        #elif self.ryn.isChecked():
        else:
            self.sRUNNING = '&is_completed='
            
            
    def searchMangaFox(self):
        
        self.updateNameMethod()
        self.updateName()
        self.updateMangaType()
        self.updateAuthorMethod()
        self.updateAuthor()
        self.updateArtistMethod()
        self.updateArtist()
        self.updateGenres()
        self.updateReleaseMethod()
        self.updateReleaseYear()
        self.updateRatingMethod()
        self.updateRating()
        self.isRunning()
        
        print('Generated search URL string:')
        print(self.generateSearchURL())
        print()
        
        #return self.generateSearchURL()
        self.mSEARCH_URL = self.generateSearchURL()
        
        '''
        c = pycurl.Curl()
        c.setopt(c.URL, self.mSEARCH_URL)
        
        with open('output.txt', 'wb') as f:
            c.setopt(c.WRITEFUNCTION, f.write)
            c.perform()
        
        c.close()
        '''
        
        '''
        # GET the page specified by the URL, scrape it and display the search results
        
        r = requests.get(self.mSEARCH_URL)
        page = r.text
        
        bs = BeautifulSoup(page, 'lxml') # parse using lxml
        
        results = bs.find_all('div', class_='manga_text')
        
        for i in results:
            print(i.find('a').get('href'))
            print(i.find('a').text + '\n')
        '''
        

#end of class GUI
