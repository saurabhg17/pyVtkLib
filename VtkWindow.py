from PyQt5 import QtWidgets
import vtk
import vtkmodules.qt
vtkmodules.qt.QVTKRWIBase = "QGLWidget"
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


# VtkWindow must be derived from QFrame: https://vtk.org/Wiki/VTK/Examples/Python/Widgets/EmbedPyQt
class VtkWindow(QtWidgets.QFrame):
	def __init__(self, parent=None):
		super(QtWidgets.QWidget, self).__init__(parent)
		
		# Create a VTK widget and add it to the QFrame.
		self.setLayout(QtWidgets.QVBoxLayout())
		self.mVtkWidget = QVTKRenderWindowInteractor(self)
		self.layout().addWidget(self.mVtkWidget)
		self.layout().setContentsMargins(0, 0, 0, 0)
		
		# Get the render window and set an interactor.
		self.mRenderWindow = self.mVtkWidget.GetRenderWindow()
		self.mInteractor   = self.mRenderWindow.GetInteractor()
		self.mInteractor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
		self.mInteractor.Initialize()
		
		# Create a new renderer and set the background color.
		self.mRenderer = vtk.vtkRenderer()
		self.setBackgroundColor([0.5, 0.5, 0.5])
		self.mRenderWindow.AddRenderer(self.mRenderer)
		
		
		# Set the Vtk Window title.
		self.mTitleActor = None
		self.setTitle("pyVtkStarter")
		
		
	# Called when QFrame is resized.
	def resizeEvent(self, newSize):
		textSize = [0, 0]
		self.mTitleActor.GetSize(self.mRenderer, textSize)
		
		width  = int( (self.width() - textSize[0]) / 2.0)
		height = self.height() - textSize[1]
		self.mTitleActor.SetPosition(width, height - 10)
		
	
	def setBackgroundColor(self, color):
		self.mRenderer.SetBackground(color)
		
	
	def setTitle(self, title):
		if not self.mTitleActor:
			self.mTitleActor = vtk.vtkTextActor()
			self.mTitleActor.GetTextProperty().SetFontFamilyAsString("Georgia")
			self.mTitleActor.GetTextProperty().SetFontSize(30)
			self.mTitleActor.GetTextProperty().SetColor([1, 0, 0])
			self.mTitleActor.SetInput(title)
			self.mTitleActor.SetPosition(0, 0)
			self.mRenderer.AddActor(self.mTitleActor)
		else:
			self.mTitleActor.SetInput(title)
	