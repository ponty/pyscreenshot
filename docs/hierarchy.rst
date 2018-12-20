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
                pyscreenshot -> Qt4GrabWindowWrapper;
                pyscreenshot -> Qt5GrabWindowWrapper;
                pyscreenshot -> PySideGrabWindowWrapper;
                pyscreenshot -> PilWrapper;
                pyscreenshot -> ImagemagickWrapper;
                pyscreenshot -> WxScreenWrapper;
                pyscreenshot -> ScrotWrapper;
                pyscreenshot -> MacQuartzWrapper
                pyscreenshot -> ScreencaptureWrapper
                pyscreenshot -> GnomeScreenshotWrapper
                pyscreenshot -> Gdk3PixbufWrapper
            }
        }
        subgraph cluster_3 {
            PIL;
            wxPython;
            PyQt4;
            PyQt5;
            PySide;
            PyGTK;
            screencapture;
            Quartz;
            Scrot;
            Imagemagick;
            "gnome-screenshot";
        }
        subgraph cluster_4 {
            label = "GUI library";
            Qt4;
            Qt5;
            wxWidgets;
            "GTK+";
        }

        Qt4GrabWindowWrapper -> PyQt4 -> Qt4;
        PyQt4 -> Qt5;
        Qt5GrabWindowWrapper -> PyQt5 -> Qt5;
        PySideGrabWindowWrapper -> PySide -> Qt4;
        Qt4 -> MacOS;
        Qt4 -> Windows;
        Qt4 -> X11;
        Qt5 -> MacOS;
        Qt5 -> Windows;
        Qt5 -> X11;

        PilWrapper -> PIL -> Windows;
        ImagemagickWrapper -> Imagemagick -> X11;
        ScrotWrapper -> Scrot -> X11;

        GnomeScreenshotWrapper -> "gnome-screenshot" -> X11;
        "gnome-screenshot" -> Wayland;

        GtkPixbufWrapper -> PyGTK -> "GTK+";
        "GTK+" -> MacOS;
        "GTK+" -> Windows;
        "GTK+" -> X11;

        Gdk3PixbufWrapper -> PyGObject -> GdkPixbuf;
        GdkPixbuf -> MacOS;
        GdkPixbuf -> Windows;
        GdkPixbuf -> X11;

        WxScreenWrapper -> wxPython -> wxWidgets;
        wxWidgets -> "GTK+";
        wxWidgets -> MacOS;
        wxWidgets -> Windows;
        wxWidgets -> X11;

        MacQuartzWrapper -> Quartz -> MacOS;
        ScreencaptureWrapper -> screencapture -> MacOS;

        application -> pyscreenshot;

    }
