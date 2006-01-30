Summary:	GNOME utility programs
Summary(ja):	GNOME ╔Ф║╪╔ф╔ё╔Й╔ф╔ё╔в╔М╔╟╔И╔Ю╫╦
Summary(pl):	Programy u©ytkowe GNOME
Summary(ru):	Утилиты GNOME, такие как поиск файлов и калькулятор
Summary(uk):	Утил╕ти GNOME, так╕ як пошук файл╕в та калькулятор
Summary(zh_CN):	GNOMEс╕сцЁлпР╪╞
Name:		gnome-utils
Version:	2.13.91
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-utils/2.13/%{name}-%{version}.tar.bz2
# Source0-md5:	270d8f73d28e2334becc9c3f2bf126c5
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-desktop-devel >= 2.10.0-2
BuildRequires:	gnome-panel-devel >= 2.10.0-2
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	hal-devel >= 0.4.7
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	gnome-vfs2 >= 2.10.0-2
Requires:	gtk+2 >= 2:2.6.4
Obsoletes:	gnome
Obsoletes:	gnome-admin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gnomehelpdir	%{_datadir}/gnome/help

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l ja
GNOME (GNU Network Object Model Environment) ╓о║╒ X Window System ╓н
╔╕╔ё╔С╔и╔╕╔ч╔м║╪╔╦╔Ц╓х╤╗д╢╓╥╓фф╟╓╞╔Ф║╪╔╤╔у╔Л╔С╔и╔Й║╪╓й GUI
╔╒╔в╔Й╔╠║╪╔╥╔Г╔С ╓х╔г╔╧╔╞╔х╔ц╔в╔д║╪╔К╫╦╓г╓╧║ё gnome-utils
╔я╔ц╔╠║╪╔╦╓о║╒ GNOME ╓н ╔Ф║╪╔ф╔ё╔Й╔ф╔ё╫╦╓г╓╧║ё
Gcalc,Gdialog,Gdiskfree, ╓╫╓╥╓ф╓╫╓нб╬ ╓╓╓М╓╓╓М╓й╔д║╪╔К╓╛╢ч╓ч╓Л╓ч╓╧║ё

%description -l pl
Programy u©ytkowe GNOME'a.

%description -l ru
Этот пакет содержит некоторые утилиты для GNOME, такие как инструмент
для поиска файлов, калькулятор, редактор 16-ричного кода и т.п.

%description -l uk
Цей пакет м╕стить деяк╕ утил╕ти для GNOME, так╕ як ╕нструмент для
пошуку файл╕в, калькулятор, редактор 16-кового коду, тощо.

%package -n libgdict
Summary:	libgdict library
Summary(pl):	Biblioteka libgdict
Group:		Libraries

%description -n libgdict
libgdict library.

%description -n libgdict -l pl
Biblioteka libgdict.

%package -n libgdict-devel
Summary:	Header files for libgdict library
Summary(pl):	Pliki nagЁСwkowe biblioteki libgdict
Group:		Development/Libraries
Requires:	libgdict = %{epoch}:%{version}-%{release}

%description -n libgdict-devel
This is the package containing the header files for libgdict library.

%description -n libgdict-devel -l pl
Ten pakiet zawiera pliki nagЁСwkowe biblioteki libgdict.

%package -n libgdict-static
Summary:	Static libgdict library
Summary(pl):	Statyczna biblioteka libgdict
Group:		Development/Libraries
Requires:	libgdict-devel = %{epoch}:%{version}-%{release}

%description -n libgdict-static
Static libgdict library.

%description -n libgdict-static -l pl
Statyczna biblioteka libgdict.

%package dictionary
Summary:	Online dictionary
Summary(pl):	SЁownik online
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	gnome-dict
Conflicts:	gnome-utils <= 0:2.10.0-1

%description dictionary
Allows to look up an online dictionary for definitions and correct
spellings of words.

%description dictionary -l pl
Pozwala na wyszukiwanie definicji i poprawnej pisowni sЁСw w sЁowniku
sieciowym.

%package floppy
Summary:	GNOME floppy formatter
Summary(pl):	Formater dyskietek dla GNOME
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description floppy
GFloppy formats floppy disks.

%description floppy -l pl
GFloppy formatuje dyskietki.

%package logview
Summary:	System log viewer for GNOME
Summary(pl):	Przegl╠darka logСw systemowych dla GNOME
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description logview
Allows to view system logs.

%description logview -l pl
Pozwala na przegl╠danie logСw systemowych.

%package search-tool
Summary:	GNOME search tool
Summary(pl):	NarzЙdzie wyszukuj╠ce dla GNOME
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description search-tool
Allows to search for files on system.

%description search-tool -l pl
Pozwala na wyszukiwanie plikСw w systemie.

%package screenshot
Summary:	Screenshot utility
Summary(pl):	NarzЙdzie do robienia zrzutСw ekranu
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description screenshot
Allows to make a desktop screenshot.

%description screenshot -l pl
Pozwala na zrobienie zrzutu ekranu biurka.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}-2.0
%find_lang gfloppy --with-gnome
%find_lang gnome-dictionary --with-gnome
%find_lang gnome-search-tool --with-gnome
%find_lang gnome-system-log --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n libgdict -p /sbin/ldconfig
%postun -n libgdict -p /sbin/ldconfig

%post dictionary
%scrollkeeper_update_post
%gconf_schema_install gnome-dictionary.schemas

%preun dictionary
%gconf_schema_uninstall gnome-dictionary.schemas

%postun dictionary
%scrollkeeper_update_postun

%post floppy
%scrollkeeper_update_post
%update_desktop_database_post
%gconf_schema_install gfloppy.schemas

%preun floppy
%gconf_schema_uninstall gfloppy.schemas

%postun floppy
%scrollkeeper_update_postun
%update_desktop_database_postun

%post logview
%scrollkeeper_update_post
%gconf_schema_install logview.schemas

%preun logview
%gconf_schema_uninstall logview.schemas

%postun logview
%scrollkeeper_update_postun

%post search-tool
%scrollkeeper_update_post
%gconf_schema_install gnome-search-tool.schemas

%preun search-tool
%gconf_schema_uninstall gnome-search-tool.schemas

%postun search-tool
%scrollkeeper_update_postun

%post screenshot
%gconf_schema_install gnome-screenshot.schemas

%preun screenshot
%gconf_schema_uninstall gnome-screenshot.schemas

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/glade

%files -n libgdict
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdict-1.0.so.*.*.*
%{_datadir}/gdict-1.0

%files -n libgdict-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdict-1.0.so
%{_libdir}/libgdict-1.0.la
%{_gtkdocdir}/gdict
%{_includedir}/gdict-1.0
%{_pkgconfigdir}/gdict-1.0.pc

%files -n libgdict-static
%defattr(644,root,root,755)
%{_libdir}/libgdict-1.0.a

%files dictionary -f gnome-dictionary.lang
%defattr(644,root,root,755)
%doc gnome-dictionary/ChangeLog gnome-dictionary/README gnome-dictionary/TODO
%attr(755,root,root) %{_bindir}/gnome-dictionary
%attr(755,root,root) %{_libdir}/gnome-dictionary-applet
%{_sysconfdir}/gconf/schemas/gnome-dictionary.schemas
%{_desktopdir}/gnome-dictionary.desktop
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/gnome-dictionary
%{_mandir}/man1/gnome-dictionary*
%{_pixmapsdir}/gnome-dictionary.png
%{_omf_dest_dir}/gnome-dictionary/gnome-dictionary-C.omf
%lang(es) %{_omf_dest_dir}/gnome-dictionary/gnome-dictionary-es.omf

%files floppy -f gfloppy.lang
%defattr(644,root,root,755)
%doc gfloppy/AUTHORS gfloppy/ChangeLog gfloppy/NEWS gfloppy/README gfloppy/TODO
%attr(755,root,root) %{_bindir}/gfloppy
%{_sysconfdir}/gconf/schemas/gfloppy.schemas
%{_desktopdir}/gfloppy.desktop
%{_datadir}/%{name}/glade/gfloppy2.glade
%{_mandir}/man1/gfloppy*
%{_omf_dest_dir}/gfloppy/gfloppy-C.omf

%files logview -f gnome-system-log.lang
%defattr(644,root,root,755)
%doc logview/ChangeLog logview/TODO
%attr(755,root,root) %{_bindir}/gnome-system-log
%{_sysconfdir}/gconf/schemas/logview.schemas
%{_desktopdir}/gnome-system-log.desktop
%{_datadir}/gnome-system-log
%{_mandir}/man1/gnome-system-log*
%{_omf_dest_dir}/gnome-system-log/gnome-system-log-C.omf
%lang(es) %{_omf_dest_dir}/gnome-system-log/gnome-system-log-es.omf

%files search-tool -f gnome-search-tool.lang
%defattr(644,root,root,755)
%doc gsearchtool/AUTHORS gsearchtool/ChangeLog
%attr(755,root,root) %{_bindir}/gnome-search-tool
%{_sysconfdir}/gconf/schemas/gnome-search-tool.schemas
%{_desktopdir}/gnome-search-tool.desktop
%{_datadir}/%{name}
%{_mandir}/man1/gnome-search-tool*
%{_pixmapsdir}/gsearchtool
%{_omf_dest_dir}/gnome-search-tool/gnome-search-tool-C.omf
%lang(es) %{_omf_dest_dir}/gnome-search-tool/gnome-search-tool-es.omf

%files screenshot
%defattr(644,root,root,755)
%doc gnome-screenshot/ChangeLog
%attr(755,root,root) %{_bindir}/gnome-panel-screenshot
%attr(755,root,root) %{_bindir}/gnome-screenshot
%{_datadir}/gnome-screenshot
%{_desktopdir}/gnome-screenshot.desktop
%{_sysconfdir}/gconf/schemas/gnome-screenshot.schemas
