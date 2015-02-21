%define _disable_ld_no_undefined 1
%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname gnome-python
%define haveorbit 1
%define pyorbit	2.0.1
%define pygtk	2.10.3

Summary:	The sources for the PyGNOME Python extension module
Name:		gnome-python2
Version:	2.28.1
Release:	15
License:	LGPLv2+
Group:		Development/GNOME and GTK+
Url:		ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python/%{url_ver}/%{oname}-%{version}.tar.bz2

BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(gconf-2.0) >= 2.11.1
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.0.0
BuildRequires:	pkgconfig(libbonoboui-2.0)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libgnome-2.0)
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python2)
Requires:	pygtk2.0 >= %{pygtk}
%if %{haveorbit}
Requires:	%{name}-bonobo
BuildRequires:	pkgconfig(pyorbit-2) >= %{pyorbit}
%endif

%description
The gnome-python package contains the source packages for the Python
bindings for GNOME called PyGNOME.

PyGNOME is an extension module for Python that provides access to the
base GNOME libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package canvas
Summary:	Python bindings for the GNOME Canvas
Group:		Development/GNOME and GTK+
Requires:	libgnomecanvas2 >= 2.0.0
Requires:	pygtk2.0 >= %{pygtk}
Requires:	%{name} = %{version}-%{release}

%description canvas
This module contains a wrapper that allows use of the GNOME Canvas
in Python.

%package bonobo
Summary:	Python bindings for interacting with bonobo
Group:		Development/GNOME and GTK+
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	pyorbit >= %{pyorbit}
Requires:	%{_lib}bonoboui2_0 >= 2.0.0

%description bonobo
This module contains a wrapper that allows the creation of bonobo
components and the embedding of bonobo components in Python.

%package gconf
Summary:	Python bindings for interacting with GConf
Group:		Development/GNOME and GTK+
Requires:	GConf2 >= 1.1.10

%description gconf
This module contains a wrapper that allows the use of GConf via Python.

%package gnomevfs
Summary:	Python bindings for interacting with gnome-vfs
Group:		Development/GNOME and GTK+
Requires:	gnome-vfs2 >= 2.0.2

%description gnomevfs
This module contains a wrapper that allows the use of gnome-vfs via python.

%package devel
Summary:	Development files of %{name}
Group:		Development/Python
Requires:	%{name} = %{version}

%description devel
Development files of the Gnome Python wrappers.

%prep
%setup -qn %{oname}-%{version}

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH
export LDFLAGS="$LDFLAGS -lpython2.7" 
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%dir %{py2_platsitedir}/gtk-2.0/gnome/
%{py2_platsitedir}/gtk-2.0/gnome/__init__.*
%{py2_platsitedir}/gtk-2.0/gnome/_gnome.so
%if %{haveorbit}
%{py2_platsitedir}/gtk-2.0/gnome/ui.so
%endif

%if %{haveorbit}
%files canvas
%{py2_platsitedir}/gtk-2.0/gnome/canvas.*
%{py2_platsitedir}/gtk-2.0/gnomecanvas.so
%doc examples/canvas
%endif

%if %{haveorbit}
%files bonobo
%dir %{py2_platsitedir}/gtk-2.0/bonobo/
%{py2_platsitedir}/gtk-2.0/bonobo/__init__.*
%{py2_platsitedir}/gtk-2.0/bonobo/*.so
%doc examples/bonobo
%endif

%files gconf
%{py2_platsitedir}/gtk-2.0/gconf*
%doc examples/gconf

%files gnomevfs
%{py2_platsitedir}/gtk-2.0/gnome/vfs*
%{py2_platsitedir}/gtk-2.0/gnomevfs
%{_libdir}/gnome-vfs-2.0/modules/libpythonmethod.so
%doc examples/vfs

%files devel
%{_includedir}/gnome-python-2.0/pygnomevfs.h
%{_includedir}/gnome-python-2.0/pygnomevfsbonobo.h
%{_libdir}/pkgconfig/gnome-python-2.0.pc
%doc %{_datadir}/gtk-doc/html/pygnomevfs
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/argtypes

