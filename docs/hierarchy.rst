Hierarchy
=========

.. graphviz::

	digraph G {
	rankdir=LR;
	node [fontsize=8];
	fontsize=8;
	
	subgraph cluster_0 {
		label = "pyscreenshot";
		style=filled;
		fillcolor=lightgrey;
		subgraph cluster_1 {
			label = "API";
			style=filled;
			fillcolor=white;

			pyscreenshot;
		}
		subgraph cluster_2 {
			style=filled;
			fillcolor=white;
			label = "plugins";

			pyscreenshot -> GtkPixbufWrapper;
			pyscreenshot -> QtGrabWindowWrapper;
			pyscreenshot -> PilWrapper;
			pyscreenshot -> ImagemagickWrapper;
			pyscreenshot -> WxScreenWrapper;
         pyscreenshot -> ScrotWrapper;
         pyscreenshot -> MacQuartzWrapper
         pyscreenshot -> ScreencaptureWrapper
		}
	}
	QtGrabWindowWrapper -> PyQt -> Qt;
	PilWrapper -> PIL -> Windows;
	ImagemagickWrapper -> Imagemagick -> X11;
	ScrotWrapper -> Scrot -> X11;
	
	GtkPixbufWrapper -> PyGTK -> "GTK+";
	WxScreenWrapper -> wxPython -> wxWidgets;
	wxWidgets -> "GTK+";
	wxWidgets -> MacOS;
	wxWidgets -> Windows;
	wxWidgets -> X11;
	
   MacQuartzWrapper -> Quartz -> MacOS;
   ScreencaptureWrapper -> screencapture -> MacOS;

	application -> pyscreenshot;
	
	}
