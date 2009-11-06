Summary:	GNOME utility programs
Summary(ja.UTF-8):	GNOME ユーティリティプログラム集
Summary(pl.UTF-8):	Programy użytkowe GNOME
Summary(ru.UTF-8):	Утилиты GNOME
Summary(uk.UTF-8):	Утиліти GNOME
Summary(zh_CN.UTF-8):	GNOME应用程序集
Name:		gnome-utils
Version:	2.28.1
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-utils/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	3c811993191ae0bbf8666405a504288a
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-panel-devel >= 2.26.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel >= 0.4
BuildRequires:	libgtop-devel >= 2.14.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Obsoletes:	gnome
Obsoletes:	gnome-admin
Obsoletes:	gnome-utils-floppy
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
Group:		X11/Libraries

%description -n libgdict
libgdict library.

%description -n libgdict -l pl.UTF-8
Biblioteka libgdict.

%package -n libgdict-devel
Summary:	Header files for libgdict library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgdict
Group:		X11/Development/Libraries
Requires:	gtk+2-devel >= 2:2.18.0
Requires:	libgdict = %{epoch}:%{version}-%{release}

%description -n libgdict-devel
This is the package containing the header files for libgdict library.

%description -n libgdict-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libgdict.

%package -n libgdict-static
Summary:	Static libgdict library
Summary(pl.UTF-8):	Statyczna biblioteka libgdict
Group:		X11/Development/Libraries
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

%build
%{__intltoolize}
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
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
%find_lang baobab --with-gnome --with-omf
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

%post logview
%scrollkeeper_update_post
%gconf_schema_install gnome-system-log.schemas

%preun logview
%gconf_schema_uninstall gnome-system-log.schemas

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

%files -n libgdict
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdict-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdict-1.0.so.6
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
%doc gnome-dictionary/AUTHORS gnome-dictionary/README gnome-dictionary/TODO
%attr(755,root,root) %{_bindir}/gnome-dictionary
%attr(755,root,root) %{_libdir}/gnome-dictionary-applet
%{_sysconfdir}/gconf/schemas/gnome-dictionary.schemas
%{_desktopdir}/gnome-dictionary.desktop
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/gnome-dictionary
%{_mandir}/man1/gnome-dictionary*

%files logview -f gnome-system-log.lang
%defattr(644,root,root,755)
%doc logview/ChangeLog logview/TODO
%attr(755,root,root) %{_bindir}/gnome-system-log
%{_sysconfdir}/gconf/schemas/gnome-system-log.schemas
%{_desktopdir}/gnome-system-log.desktop
%{_datadir}/%{name}/logview-filter.ui
%{_datadir}/%{name}/logview-toolbar.xml
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
%{_mandir}/man1/gnome-screenshot*
