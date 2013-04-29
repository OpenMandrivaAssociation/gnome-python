%define haveorbit 1
%define pyorbit 2.0.1
%define pygtk 2.10.3
%define _disable_ld_no_undefined 1

Summary: The sources for the PyGNOME Python extension module
Name: gnome-python
Version: 2.28.1
Release: 8
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python/gnome-python-%{version}.tar.bz2
URL: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python/
License: LGPLv2+
Group: Development/GNOME and GTK+
BuildRequires: python-gobject-devel >= 2.17.0
BuildRequires: pygtk2.0-devel >= %pygtk
BuildRequires: python-devel >= 2.2
BuildRequires: pkgconfig(gtk+-2.0) >= 2.0.0
BuildRequires: libgnome2-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libgnomecanvas2-devel
BuildRequires: pkgconfig(libbonoboui-2.0)
BuildRequires: pkgconfig(gconf-2.0) >= 2.11.1
BuildRequires: avahi-glib-devel avahi-client-devel
BuildRequires: libgcrypt-devel
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

%package devel
Summary: Development files of %name
Group: Development/Python
Requires: %name = %version
Conflicts: %name < 2.21.0

%description devel
Development files of the Gnome Python wrappers.

%prep
%setup -q -n gnome-python-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

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
%defattr(644,root,root,755)
%doc examples/vfs

%files devel
%defattr(-,root,root)
%{_includedir}/gnome-python-2.0/pygnomevfs.h
%{_includedir}/gnome-python-2.0/pygnomevfsbonobo.h
%doc %_datadir/gtk-doc/html/pygnomevfs
%{_libdir}/pkgconfig/gnome-python-2.0.pc
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/argtypes


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.28.1-3mdv2011.0
+ Revision: 664881
- mass rebuild

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 2.28.1-2mdv2011.0
+ Revision: 591290
- rebuild for py2.7

* Wed Mar 31 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.1-1mdv2010.1
+ Revision: 530221
- update to new version 2.28.1

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-2mdv2010.1
+ Revision: 521489
- rebuilt for 2010.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446621
- update to new version 2.28.0

* Wed May 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.1-2mdv2010.0
+ Revision: 380111
- rebuild for new gdl

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374376
- new version
- bump pygobject dep

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366982
- update to new version 2.26.1

* Sat Mar 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355138
- update to new version 2.26.0

* Mon Feb 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.90-2mdv2009.1
+ Revision: 336410
- fukc se BS
- new version
- drop merged patch

* Fri Jan 30 2009 Funda Wang <fwang@mandriva.org> 2.25.1-3mdv2009.1
+ Revision: 335644
- rework linkage patch to be submitted upstream

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 2.25.1-2mdv2009.1
+ Revision: 330841
- fix linkage

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 330835
- New version 2.25.1

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 2.22.3-2mdv2009.1
+ Revision: 318620
- rebuild for python 2.6
- drop unnecessary autotools br

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 286598
- new version

* Sun Sep 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 286339
- new version

* Mon Jun 16 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 219379
- new version
- clean spec file

* Sun Mar 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183053
- new version

* Sun Feb 24 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 174266
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.0-1mdv2008.1
+ Revision: 115243
- new version
- split out devel package

* Sat Nov 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 111791
- new version

* Sun Sep 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 88451
- new version

* Tue Jul 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.2-1mdv2008.0
+ Revision: 56952
- fix buildrequires
- new version

* Sat Jul 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-2mdv2008.0
+ Revision: 49450
- new version

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 14165
- new version


* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 141949
- new version

* Sun Feb 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 125670
- new version

* Mon Jan 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2-1mdv2007.1
+ Revision: 106022
- new version

* Sun Jan 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.1-1mdv2007.1
+ Revision: 105300
- new version

* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.2-3mdv2007.1
+ Revision: 88192
- bump release
- fix buildrequires
- rebuild

* Mon Nov 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.2-1mdv2007.1
+ Revision: 76838
- mkrel
- Import gnome-python

* Sun Nov 05 2006 Götz Waschk <waschk@mandriva.org> 2.16.2-1
- bump deps
- New version 2.16.2

* Wed Sep 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New version 2.16.0

* Wed Aug 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1mdv2007.0
- update file list
- New release 2.15.90

* Fri Jul 14 2006 Götz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- drop the patch
- New release 2.15.4

* Thu Jul 13 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-3mdv2007.0
- fix the patch (Oops!)

* Thu Jul 13 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-2mdv2007.0
- fix build with new gnome-vfs/libbonobo

* Wed Jul 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.3-1
- New release 2.15.3

* Tue Jun 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.2-1mdv2007.0
- New release 2.15.2

* Wed Jun 07 2006 Götz Waschk <waschk@mandriva.org> 2.15.1-1mdv2007.0
- drop the patch, it is obsolete
- New release 2.15.1

* Sun Mar 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.4-1mdk
- New release 2.12.4

* Thu Dec 22 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-1mdk
- New release 2.12.3
- use mkrel

* Thu Dec 01 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2

* Fri Oct 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-2mdk
- Fix buildrequires

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.12.0

* Sun Apr 24 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.10.0-2mdk
- add some gnome buildrequires

* Sat Apr 23 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-1mdk 
- Release 2.10.0 (based on Götz Waschk package)
- drop nautilus, gnomeprint, gtkhtml, applet subpackages

* Mon Dec 27 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- New release 2.6.2

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 2.6.1-2mdk
- Rebuild for new python

* Tue Nov 16 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- New release 2.6.1

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.0-1mdk
- requires new pygtk
- remove all zvt references
- drop patch 0
- New release 2.6.0

* Mon Aug 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.3-1mdk
- fix source URL
- New release 2.0.3

* Fri May 14 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.2-3mdk
- fix deps

* Wed Apr 14 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.2-2mdk
- fix buildrequires

* Wed Apr 07 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.2-1mdk
- really disable zvt
- new version

