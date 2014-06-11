# TODO:
# - cleanup
#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtmultimedia
%define		qtbase_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 Multimedia libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Multimedia
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	2d0f9403f607f617bcc13d4814f41365
URL:		http://qt-project.org/
BuildRequires:	OpenAL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	gstreamer-devel
BuildRequires:	pulseaudio-devel
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	qt5-qtbase-devel >= %{qtbase_ver}
BuildRequires:	qt5-qttools-devel >= %{qttools_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Multimedia libraries.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera biblioteki Qt5 Multimedia.

%package -n Qt5Multimedia
Summary:	The Qt5 Multimedia library
Summary(pl.UTF-8):	Biblioteka Qt5 Multimedia
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtmultimedia

%description -n Qt5Multimedia
Qt5 Multimedia library provides (TODO: ...).

%description -n Qt5Multimedia -l pl.UTF_8
Biblioteka Qt5 Multimedia dostarcza (TODO: ...).

%package -n Qt5Multimedia-devel
Summary:	Qt5 Multimedia libraries - development files
Summary(pl.UTF-8):	Biblioteki Qt5 Multimedia - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Multimedia = %{version}-%{release}
Obsoletes:	qt5-qtmultimedia-devel

%description -n Qt5Multimedia-devel
Qt5 Multimedia libraries - development files.

%description -n Qt5Multimedia-devel -l pl.UTF-8
Biblioteki Qt5 Multimedia - pliki programistyczne.

%package doc
Summary:	Qt5 Multimedia documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Multimedia w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Multimedia documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Multimedia w formacie HTML.

%package doc-qch
Summary:	Qt5 Multimedia documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Multimedia w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 Multimedia documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Multimedia w formacie QCH.

%package examples
Summary:	Qt5 Multimedia examples
Summary(pl.UTF-8):	Przykłady do bibliotek Qt5 Multimedia
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Multimedia examples.

%description examples -l pl.UTF-8
Przykłady do bibliotek Qt5 Multimedia.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# Prepare some files list
ifecho() {
	RESULT=`echo $RPM_BUILD_ROOT$2 2>/dev/null`
	[ "$RESULT" == "" ] && return # XXX this is never true due $RPM_BUILD_ROOT being set
	r=`echo $RESULT | awk '{ print $1 }'`

	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho examples %{_examplesdir}/qt5
for f in `find $RPM_BUILD_ROOT%{_examplesdir}/qt5 -printf "%%P "`; do
	ifecho examples %{_examplesdir}/qt5/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Multimedia -p /sbin/ldconfig
%postun	-n Qt5Multimedia -p /sbin/ldconfig

%files -n Qt5Multimedia
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Multimedia.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Multimedia.so.5
%attr(755,root,root) %{_libdir}/libQt5MultimediaQuick_p.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5MultimediaQuick_p.so.5
%attr(755,root,root) %{_libdir}/libQt5MultimediaWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5MultimediaWidgets.so.5
%attr(755,root,root) %{_libdir}/libqgsttools_p.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqgsttools_p.so.?
%attr(755,root,root) %{qt5dir}/plugins/*
%{qt5dir}/qml/*

%files -n Qt5Multimedia-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Multimedia.so
%attr(755,root,root) %{_libdir}/libQt5MultimediaQuick_p.so
%attr(755,root,root) %{_libdir}/libQt5MultimediaWidgets.so
%attr(755,root,root) %{_libdir}/libqgsttools_p.so
%{_libdir}/libQt5Multimedia.prl
%{_libdir}/libQt5MultimediaQuick_p.prl
%{_libdir}/libQt5MultimediaWidgets.prl
%{_libdir}/libqgsttools_p.prl
%{_includedir}/qt5/QtMultimedia
%{_includedir}/qt5/QtMultimediaQuick_p
%{_includedir}/qt5/QtMultimediaWidgets
%{_pkgconfigdir}/Qt5Multimedia.pc
%{_pkgconfigdir}/Qt5MultimediaQuick_p.pc
%{_pkgconfigdir}/Qt5MultimediaWidgets.pc
%{_libdir}/cmake/Qt5Multimedia
%{_libdir}/cmake/Qt5MultimediaWidgets
%{qt5dir}/mkspecs/modules/*.pri

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtmultimedia

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtmultimedia.qch
%endif

%files examples -f examples.files
