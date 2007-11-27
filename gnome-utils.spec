Summary:	GNOME utility programs
Summary(ja.UTF-8):	GNOME ユーティリティプログラム集
Summary(pl.UTF-8):	Programy użytkowe GNOME
Summary(ru.UTF-8):	Утилиты GNOME, такие как поиск файлов и калькулятор
Summary(uk.UTF-8):	Утиліти GNOME, такі як пошук файлів та калькулятор
Summary(zh_CN.UTF-8):	GNOME应用程序集
Name:		gnome-utils
Version:	2.20.0
Release:	5
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-utils/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	f58f05a1eac5b04d2ebd66fcc2606251
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-desktop-devel >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-panel-devel >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonoboui-devel >= 2.20.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeprintui-devel >= 2.18.0
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libgtop-devel >= 2.14.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gnome-vfs2 >= 2.20.0
Requires:	libgnomeui >= 2.20.0
Obsoletes:	gnome
Obsoletes:	gnome-admin
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l ja.UTF-8
GNOME (GNU Network Object Model Environment) は、 X Window System の
ウィンドウマネージャと協調して動くユーザフレンドリーな GUI
アプリケーション とデスクトップツール集です。 gnome-utils
パッケージは、 GNOME の ユーティリティ集です。
Gcalc,Gdialog,Gdiskfree, そしてその他 いろいろなツールが含まれます。

%description -l pl.UTF-8
Programy użytkowe GNOME'a.

%description -l ru.UTF-8
Этот пакет содержит некоторые утилиты для GNOME, такие как инструмент
для поиска файлов, калькулятор, редактор 16-ричного кода и т.п.

%description -l uk.UTF-8
Цей пакет містить деякі утиліти для GNOME, такі як інструмент для
пошуку файлів, калькулятор, редактор 16-кового коду, тощо.

%package -n libgdict
Summary:	libgdict library
Summary(pl.UTF-8):	Biblioteka libgdict
Group:		Libraries

%description -n libgdict
libgdict library.

%description -n libgdict -l pl.UTF-8
Biblioteka libgdict.

%package -n libgdict-devel
Summary:	Header files for libgdict library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgdict
Group:		Development/Libraries
Requires:	libgdict = %{epoch}:%{version}-%{release}

%description -n libgdict-devel
This is the package containing the header files for libgdict library.

%description -n libgdict-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libgdict.

%package -n libgdict-static
Summary:	Static libgdict library
Summary(pl.UTF-8):	Statyczna biblioteka libgdict
Group:		Development/Libraries
Requires:	libgdict-devel = %{epoch}:%{version}-%{release}

%description -n libgdict-static
Static libgdict library.

%description -n libgdict-static -l pl.UTF-8
Statyczna biblioteka libgdict.

%package -n libgdict-apidocs
Summary:	libgdict API documentation
Summary(pl.UTF-8):	Dokumentacja API libgdict
Group:		Documentation
Requires:	gtk-doc-common

%description -n libgdict-apidocs
libgdict API documentation.

%description -n libgdict-apidocs -l pl.UTF-8
Dokumentacja API libgdict.

%package baobab
Summary:	Graphical directory tree analyzer
Summary(pl.UTF-8):	Graficzny analizator drzew katalogów
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	baobab

%description baobab
Graphical directory tree analyzer.

%description baobab -l pl.UTF-8
Graficzny analizator drzew katalogów.

%package dictionary
Summary:	Online dictionary
Summary(pl.UTF-8):	Słownik online
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gnome-utils-dict
Obsoletes:	gnome-dict
Obsoletes:	gnome-utils-dict
Conflicts:	gnome-utils <= 0:2.10.0-1

%description dictionary
Allows to look up an online dictionary for definitions and correct
spellings of words.

%description dictionary -l pl.UTF-8
Pozwala na wyszukiwanie definicji i poprawnej pisowni słów w słowniku
sieciowym.

%package floppy
Summary:	GNOME floppy formatter
Summary(pl.UTF-8):	Formater dyskietek dla GNOME
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description floppy
GFloppy formats floppy disks.

%description floppy -l pl.UTF-8
GFloppy formatuje dyskietki.

%package logview
Summary:	System log viewer for GNOME
Summary(pl.UTF-8):	Przeglądarka logów systemowych dla GNOME
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description logview
Allows to view system logs.

%description logview -l pl.UTF-8
Pozwala na przeglądanie logów systemowych.

%package search-tool
Summary:	GNOME search tool
Summary(pl.UTF-8):	Narzędzie wyszukujące dla GNOME
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description search-tool
Allows to search for files on system.

%description search-tool -l pl.UTF-8
Pozwala na wyszukiwanie plików w systemie.

%package screenshot
Summary:	Screenshot utility
Summary(pl.UTF-8):	Narzędzie do robienia zrzutów ekranu
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description screenshot
Allows to make a desktop screenshot.

%description screenshot -l pl.UTF-8
Pozwala na zrobienie zrzutu ekranu biurka.

%prep
%setup -q
%patch0 -p1

sed -i -e 's#sr\@Latn#sr\@latin#' po/LINGUAS
mv -f po/sr\@{Latn,latin}.po

%build
%{__intltoolize}
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-gfloppy \
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
%find_lang baobab --with-gnome --with-omf
%find_lang gfloppy --with-gnome --with-omf
%find_lang gnome-dictionary --with-gnome --with-omf
%find_lang gnome-search-tool --with-gnome --with-omf
%find_lang gnome-system-log --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n libgdict -p /sbin/ldconfig
%postun -n libgdict -p /sbin/ldconfig

%post baobab
%scrollkeeper_update_post
%gconf_schema_install baobab.schemas
%update_icon_cache hicolor

%preun baobab
%gconf_schema_uninstall baobab.schemas

%postun baobab
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post dictionary
%scrollkeeper_update_post
%gconf_schema_install gnome-dictionary.schemas
%update_icon_cache hicolor

%preun dictionary
%gconf_schema_uninstall gnome-dictionary.schemas

%postun dictionary
%scrollkeeper_update_postun
%update_icon_cache hicolor

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
%{_includedir}/gdict-1.0
%{_pkgconfigdir}/gdict-1.0.pc

%files -n libgdict-static
%defattr(644,root,root,755)
%{_libdir}/libgdict-1.0.a

%files -n libgdict-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdict

%files baobab -f baobab.lang
%defattr(644,root,root,755)
%doc baobab/AUTHORS baobab/ChangeLog baobab/README baobab/TODO
%attr(755,root,root) %{_bindir}/baobab
%{_sysconfdir}/gconf/schemas/baobab.schemas
%{_desktopdir}/baobab.desktop
%{_iconsdir}/hicolor/*/*/baobab.*
%{_datadir}/baobab
%{_mandir}/man1/baobab*

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

%files floppy -f gfloppy.lang
%defattr(644,root,root,755)
%doc gfloppy/AUTHORS gfloppy/ChangeLog gfloppy/NEWS gfloppy/README gfloppy/TODO
%attr(755,root,root) %{_bindir}/gfloppy
%{_sysconfdir}/gconf/schemas/gfloppy.schemas
%{_desktopdir}/gfloppy.desktop
%{_datadir}/%{name}/glade/gfloppy2.glade
%{_mandir}/man1/gfloppy*

%files logview -f gnome-system-log.lang
%defattr(644,root,root,755)
%doc logview/ChangeLog logview/TODO
%attr(755,root,root) %{_bindir}/gnome-system-log
%{_sysconfdir}/gconf/schemas/logview.schemas
%{_desktopdir}/gnome-system-log.desktop
%{_datadir}/gnome-system-log
%{_mandir}/man1/gnome-system-log*

%files search-tool -f gnome-search-tool.lang
%defattr(644,root,root,755)
%doc gsearchtool/AUTHORS gsearchtool/ChangeLog
%attr(755,root,root) %{_bindir}/gnome-search-tool
%{_sysconfdir}/gconf/schemas/gnome-search-tool.schemas
%{_desktopdir}/gnome-search-tool.desktop
%{_mandir}/man1/gnome-search-tool*
%{_pixmapsdir}/gsearchtool

%files screenshot
%defattr(644,root,root,755)
%doc gnome-screenshot/ChangeLog
%attr(755,root,root) %{_bindir}/gnome-panel-screenshot
%attr(755,root,root) %{_bindir}/gnome-screenshot
%{_datadir}/gnome-screenshot
%{_desktopdir}/gnome-screenshot.desktop
%{_sysconfdir}/gconf/schemas/gnome-screenshot.schemas
