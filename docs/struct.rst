Hierarchy
==================================

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
		}
	}
	QtGrabWindowWrapper -> PyQt -> Qt;
	PilWrapper -> PIL;
	ImagemagickWrapper -> Imagemagick;
	ScrotWrapper -> Scrot;
	
	GtkPixbufWrapper -> PyGTK -> "GTK+";
	WxScreenWrapper -> wxPython -> wxWidgets;
	wxWidgets -> "GTK+";
	wxWidgets -> MacOS;
	wxWidgets -> Windows;
	//wxWidgets -> "Palm OS";
	wxWidgets -> X11;
	
	application -> pyscreenshot;
	
	}
   