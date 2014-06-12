#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtmultimedia
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Multimedia libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Multimedia
Name:		qt5-%{orgname}
Version:	5.3.0
Release:	1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.3/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	921f4596ca39b78851663369db0bbcee
URL:		http://qt-project.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
BuildRequires:	Qt5Xml-devel >= %{qtbase_ver}
BuildRequires:	alsa-lib-devel
BuildRequires:	gstreamer0.10-devel >= 0.10
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10
BuildRequires:	pulseaudio-devel
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
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
Summary:	The Qt5 Multimedia libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Multimedia
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5OpenGL >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
Obsoletes:	qt5-qtmultimedia

%description -n Qt5Multimedia
Qt5 Multimedia libraries provide audio, video, radio and camera
functionality.

%description -n Qt5Multimedia -l pl.UTF_8
Biblioteki Qt5 Multimedia dostarczają funkcjonalność związaną z
dźwiękiem, obrazem, radiem i kamerą.

%package -n Qt5Multimedia-devel
Summary:	Qt5 Multimedia libraries - development files
Summary(pl.UTF-8):	Biblioteki Qt5 Multimedia - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	OpenGL-devel
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Multimedia = %{version}-%{release}
Requires:	Qt5Quick-devel >= %{qtdeclarative_ver}
Requires:	Qt5Widgets-devel >= %{qtbase_ver}
Requires:	pulseaudio-devel
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

# kill unnecessary -L%{_libdir} from *.la, *.prl, *.pc
%{__sed} -i -e "s,-L%{_libdir} \?,,g" \
	$RPM_BUILD_ROOT%{_libdir}/*.{la,prl} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqgsttools_p.so.1.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
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
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/multimedia
ifecho_tree examples %{_examplesdir}/qt5/multimediawidgets

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
%attr(755,root,root) %ghost %{_libdir}/libqgsttools_p.so.1
%dir %{qt5dir}/plugins/audio
# R: Qt5Core Qt5Multimedia pulseaudio-libs
%attr(755,root,root) %{qt5dir}/plugins/audio/libqtmedia_pulse.so
%dir %{qt5dir}/plugins/mediaservice
# R: Qt5Core Qt5Multimedia[+libqgsttools_p] gstreamer0.10 gstreamer0.10-plugins-base
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstaudiodecoder.so
# R: Qt5Core Qt5Gui Qt5Multimedia[+libqgsttools_p] gstreamer0.10 gstreamer0.10-plugins-base
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstcamerabin.so
# R: Qt5Core Qt5Gui Qt5Multimedia[+libqgsttools_p] gstreamer0.10
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstmediacapture.so
# R: Qt5Core Qt5Multimedia[+libqgsttools_p] gstreamer0.10
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstmediaplayer.so
%dir %{qt5dir}/plugins/playlistformats
# R: Qt5Core Qt5Multimedia
%attr(755,root,root) %{qt5dir}/plugins/playlistformats/libqtmultimedia_m3u.so
%dir %{qt5dir}/qml/QtAudioEngine
# R: Qt5Core Qt5Gui Qt5Multimedia Qt5Qml OpenAL
%attr(755,root,root) %{qt5dir}/qml/QtAudioEngine/libdeclarative_audioengine.so
%{qt5dir}/qml/QtAudioEngine/plugins.qmltypes
%{qt5dir}/qml/QtAudioEngine/qmldir
%dir %{qt5dir}/qml/QtMultimedia
# R: Qt5Core Qt5Gui Qt5Multimedia[+libQt5MultimediaQuick_p] Qt5Qml Qt5Quick
%attr(755,root,root) %{qt5dir}/qml/QtMultimedia/libdeclarative_multimedia.so
%{qt5dir}/qml/QtMultimedia/Video.qml
%{qt5dir}/qml/QtMultimedia/plugins.qmltypes
%{qt5dir}/qml/QtMultimedia/qmldir

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
%{qt5dir}/mkspecs/modules/qt_lib_multimedia.pri
%{qt5dir}/mkspecs/modules/qt_lib_multimedia_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_multimediawidgets.pri
%{qt5dir}/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtmultimedia
%{_docdir}/qt5-doc/qtmultimediawidgets

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtmultimedia.qch
%{_docdir}/qt5-doc/qtmultimediawidgets.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
