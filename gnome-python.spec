%define haveorbit 1
%define pyorbit 2.0.1
%define pygtk 2.10.3

Summary: The sources for the PyGNOME Python extension module
Name: gnome-python
Version: 2.18.2
Release: %mkrel 1
Source: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python/gnome-python-%{version}.tar.bz2
URL: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python/
License: LGPL
Group: Development/GNOME and GTK+
BuildRoot: %{_tmppath}/gnome-python-root
BuildRequires: pygtk2.0-devel >= %pygtk
BuildRequires: python-devel >= 2.2
BuildRequires: libgtk+2-devel >= 2.0.0
BuildRequires: libgnome2-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libgnomecanvas2-devel
BuildRequires: libbonoboui2-devel
BuildRequires: libGConf2-devel >= 2.11.1
BuildRequires: avahi-glib-devel avahi-client-devel
BuildRequires: autoconf2.5 automake1.9
Requires: pygtk2.0 >= %pygtk
%if %{haveorbit}
Requires: %name-bonobo
BuildRequires: pyorbit-devel >= %pyorbit
%endif

%description
The gnome-python package contains the source packages for the Python
bindings for GNOME called PyGNOME.

PyGNOME is an extension module for Python that provides access to the
base GNOME libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package capplet
Version: %{version}
Summary: Python bindings for GNOME Panel applets
Group: Development/GNOME and GTK+

%description capplet
This module contains a wrapper that allows GNOME Control Center
capplets to be in Python.

%package canvas
Version: %{version}
Summary: Python bindings for the GNOME Canvas
Group: Development/GNOME and GTK+
Requires: libgnomecanvas2 >= 2.0.0
Requires: pygtk2.0 >= %pygtk
Requires: %name = %version-%release

%description canvas
This module contains a wrapper that allows use of the GNOME Canvas
in Python.

%package bonobo
Version: %{version}
Summary: Python bindings for interacting with bonobo
Group: Development/GNOME and GTK+
Requires: %name-canvas = %version-%release
Requires: pyorbit >= %pyorbit
Requires: libbonoboui2 >= 2.0.0

%description bonobo
This module contains a wrapper that allows the creation of bonobo
components and the embedding of bonobo components in Python.

%package gconf
Version: %{version}
Summary: Python bindings for interacting with GConf
Group: Development/GNOME and GTK+
Requires: GConf2 >= 1.1.10

%description gconf
This module contains a wrapper that allows the use of GConf via Python.

%package gnomevfs
Version: %{version}
Summary: Python bindings for interacting with gnome-vfs
Group: Development/GNOME and GTK+
Requires: gnome-vfs2 >= 2.0.2

%description gnomevfs
This module contains a wrapper that allows the use of gnome-vfs via python.

%prep
%setup -q -n gnome-python-%{version}

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;

%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%defattr(755,root,root,755)
%dir %py_platsitedir/gtk-2.0/gnome/
%py_platsitedir/gtk-2.0/gnome/__init__.*
%py_platsitedir/gtk-2.0/gnome/_gnome.so
%if %{haveorbit}
%py_platsitedir/gtk-2.0/gnome/ui.so
%endif
%{_libdir}/pkgconfig/gnome-python-2.0.pc
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/argtypes

%if %{haveorbit}
%files canvas
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gnome/canvas.*
%py_platsitedir/gtk-2.0/gnomecanvas.so
%defattr(644,root,root,755)
%doc examples/canvas
%endif


%if %{haveorbit}
%files bonobo
%defattr(755,root,root,755)
%dir %py_platsitedir/gtk-2.0/bonobo/
%py_platsitedir/gtk-2.0/bonobo/__init__.*
%py_platsitedir/gtk-2.0/bonobo/*.so
%defattr(644,root,root,755)
%doc examples/bonobo
%endif

%files gconf
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gconf*
%defattr(644,root,root,755)
%doc examples/gconf

%files gnomevfs
%defattr(755,root,root,755)
%py_platsitedir/gtk-2.0/gnome/vfs*
%py_platsitedir/gtk-2.0/gnomevfs
%{_libdir}/gnome-vfs-2.0/modules/libpythonmethod.so
%{_includedir}/gnome-python-2.0/pygnomevfs.h
%{_includedir}/gnome-python-2.0/pygnomevfsbonobo.h
%defattr(644,root,root,755)
%doc examples/vfs
