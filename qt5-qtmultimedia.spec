#
# Conditional build:
%bcond_without	qch	# documentation in QCH format
%bcond_without	qm	# QM translations

%define		orgname		qtmultimedia
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Multimedia libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Multimedia
Name:		qt5-%{orgname}
Version:	5.4.1
Release:	1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.4/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	7412a5c62da71b44b9f29e29fdc6af4d
Source1:	http://download.qt-project.org/official_releases/qt/5.4/%{version}/submodules/qttranslations-opensource-src-%{version}.tar.xz
# Source1-md5:	0bdd1b0a83b03a04a4ebeedfa3057d21
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
%{?with_qm:BuildRequires:	qt5-linguist >= %{qttools_ver}}
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
Obsoletes:	qt5-qtmultimedia

%description -n Qt5Multimedia
Qt5 Multimedia libraries provide audio, video, radio and camera
functionality.

%description -n Qt5Multimedia -l pl.UTF-8
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
Requires:	pulseaudio-devel
Obsoletes:	qt5-qtmultimedia-devel

%description -n Qt5Multimedia-devel
Qt5 Multimedia libraries - development files.

%description -n Qt5Multimedia-devel -l pl.UTF-8
Biblioteki Qt5 Multimedia - pliki programistyczne.

%package -n Qt5MultimediaQuick
Summary:	Qt5 Multimedia Quick library and modules
Summary(pl.UTF-8):	Biblioteka i moduły Qt5 Multimedia Quick
Group:		X11/Libraries
Requires:	Qt5Multimedia = %{version}-%{release}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}

%description -n Qt5MultimediaQuick
Qt5 Multimedia Quick library and modules.

%description -n Qt5MultimediaQuick -l pl.UTF-8
Biblioteka i moduły Qt5 Multimedia Quick.

%package -n Qt5MultimediaQuick-devel
Summary:	Qt5 Multimedia Quick library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Multimedia Quick - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5MultimediaQuick = %{version}-%{release}
Requires:	Qt5Multimedia-devel = %{version}-%{release}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Requires:	Qt5Quick-devel >= %{qtdeclarative_ver}

%description -n Qt5MultimediaQuick-devel
Qt5 Multimedia Quick library - development files.

%description -n Qt5MultimediaQuick-devel -l pl.UTF-8
Biblioteka Qt5 Multimedia Quick - pliki programistyczne.

%package -n Qt5MultimediaWidgets
Summary:	Qt5 Multimedia Widgets library
Summary(pl.UTF-8):	Biblioteka Qt5 Multimedia Widgets
Group:		X11/Libraries
Requires:	Qt5Multimedia = %{version}-%{release}
Requires:	Qt5OpenGL >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}

%description -n Qt5MultimediaWidgets
Qt5 Multimedia Widgets library provides widgets classes for Qt5
Multimedia.

%description -n Qt5MultimediaWidgets -l pl.UTF-8
Biblioteka Qt5 Multimedia Widgets dostarcza klasy widgetów dla
biblioteki Qt5 Multimedia.

%package -n Qt5MultimediaWidgets-devel
Summary:	Qt5 Multimedia Widgets library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Multimedia Widgets - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5MultimediaWidgets = %{version}-%{release}
Requires:	Qt5Multimedia-devel = %{version}-%{release}
Requires:	Qt5OpenGL-devel >= %{qtbase_ver}
Requires:	Qt5Widgets-devel >= %{qtbase_ver}

%description -n Qt5MultimediaWidgets-devel
Qt5 Multimedia Widgets library - development files.

%description -n Qt5MultimediaWidgets-devel -l pl.UTF-8
Biblioteka Qt5 Multimedia Widgets - pliki programistyczne.

%package -n Qt5Multimedia-gstreamer
Summary:	Qt5 Multimedia GStreamer components
Summary(pl.UTF-8):	Komponenty GStreamera biblioteki Qt5 Multimedia
Group:		X11/Libraries
Requires:	Qt5MultimediaWidgets = %{version}-%{release}

%description -n Qt5Multimedia-gstreamer
Qt5 Multimedia GStreamer components (libqgsttools library and modules
for audio decoding, camera, media capturing and media playing).

%description -n Qt5Multimedia-gstreamer -l pl.UTF-8
Komponenty GStreamera biblioteki Qt5 Multimedia: biblioteka
libqgsttools, moduły do dekodowania dźwięku, kamery, przechwytywania
obrazu i odtwarzania).

%package -n Qt5Multimedia-gstreamer-devel
Summary:	Qt5 Multimedia GStreamer components - development files
Summary(pl.UTF-8):	Komponenty GStreamera biblioteki Qt5 Multimedia - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5Multimedia-gstreamer = %{version}-%{release}
Requires:	Qt5MultimediaWidgets-devel = %{version}-%{release}

%description -n Qt5Multimedia-gstreamer-devel
Qt5 Multimedia GStreamer components - development files.

%description -n Qt5Multimedia-gstreamer-devel -l pl.UTF-8
Komponenty GStreamera biblioteki Qt5 Multimedia - pliki
programistyczne.

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
%setup -q -n %{orgname}-opensource-src-%{version} %{?with_qm:-a1}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%if %{with qm}
cd qttranslations-opensource-src-%{version}
qmake-qt5
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with qm}
%{__make} -C qttranslations-opensource-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only qtmultimedia
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{assistant,designer,linguist,qmlviewer,qt,qtbase,qtconfig,qtconnectivity,qtdeclarative,qtlocation,qtquick1,qtscript,qtxmlpatterns}_*.qm
%endif

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

# find_lang --with-qm supports only PLD qt3/qt4 specific %{_datadir}/locale/*/LC_MESSAGES layout
find_qt5_qm()
{
	name="$1"
	find $RPM_BUILD_ROOT%{_datadir}/qt5/translations -name "${name}_*.qm" | \
		sed -e "s:^$RPM_BUILD_ROOT::" \
		    -e 's:\(.*/'$name'_\)\([a-z][a-z][a-z]\?\)\(_[A-Z][A-Z]\)\?\(\.qm\)$:%lang(\2\3) \1\2\3\4:'
}

echo '%defattr(644,root,root,755)' > qtmultimedia.lang
%if %{with qm}
find_qt5_qm qtmultimedia >> qtmultimedia.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Multimedia -p /sbin/ldconfig
%postun	-n Qt5Multimedia -p /sbin/ldconfig

%post	-n Qt5MultimediaQuick -p /sbin/ldconfig
%postun	-n Qt5MultimediaQuick -p /sbin/ldconfig

%post	-n Qt5MultimediaWidgets -p /sbin/ldconfig
%postun	-n Qt5MultimediaWidgets -p /sbin/ldconfig

%post	-n Qt5Multimedia-gstreamer -p /sbin/ldconfig
%postun	-n Qt5Multimedia-gstreamer -p /sbin/ldconfig

%files -n Qt5Multimedia -f qtmultimedia.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Multimedia.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Multimedia.so.5
%dir %{qt5dir}/plugins/audio
# R: Qt5Core Qt5Multimedia pulseaudio-libs
# (not splitting as libQt5Multimedia itself is linked with libpulse)
%attr(755,root,root) %{qt5dir}/plugins/audio/libqtmedia_pulse.so
%dir %{qt5dir}/plugins/mediaservice
%dir %{qt5dir}/plugins/playlistformats
# R: Qt5Core Qt5Multimedia
%attr(755,root,root) %{qt5dir}/plugins/playlistformats/libqtmultimedia_m3u.so
# common for base -devel and plugin-specific files
%dir %{_libdir}/cmake/Qt5Multimedia

%files -n Qt5Multimedia-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Multimedia.so
%{_libdir}/libQt5Multimedia.prl
%{_includedir}/qt5/QtMultimedia
%{_pkgconfigdir}/Qt5Multimedia.pc
%{_libdir}/cmake/Qt5Multimedia/Qt5MultimediaConfig*.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QM3uPlaylistPlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QPulseAudioPlugin.cmake
%{qt5dir}/mkspecs/modules/qt_lib_multimedia.pri
%{qt5dir}/mkspecs/modules/qt_lib_multimedia_private.pri

%files -n Qt5MultimediaQuick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5MultimediaQuick_p.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5MultimediaQuick_p.so.5
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

%files -n Qt5MultimediaQuick-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5MultimediaQuick_p.so
%{_libdir}/libQt5MultimediaQuick_p.prl
%{_includedir}/qt5/QtMultimediaQuick_p
%{_pkgconfigdir}/Qt5MultimediaQuick_p.pc
%{qt5dir}/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri

%files -n Qt5MultimediaWidgets
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5MultimediaWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5MultimediaWidgets.so.5

%files -n Qt5MultimediaWidgets-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5MultimediaWidgets.so
%{_libdir}/libQt5MultimediaWidgets.prl
%{_includedir}/qt5/QtMultimediaWidgets
%{_pkgconfigdir}/Qt5MultimediaWidgets.pc
%{_libdir}/cmake/Qt5MultimediaWidgets
%{qt5dir}/mkspecs/modules/qt_lib_multimediawidgets.pri
%{qt5dir}/mkspecs/modules/qt_lib_multimediawidgets_private.pri

%files -n Qt5Multimedia-gstreamer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqgsttools_p.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqgsttools_p.so.1
# R: Qt5Core Qt5Multimedia[+libqgsttools_p] gstreamer0.10 gstreamer0.10-plugins-base
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstaudiodecoder.so
# R: Qt5Core Qt5Gui Qt5Multimedia[+libqgsttools_p] gstreamer0.10 gstreamer0.10-plugins-base
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstcamerabin.so
# R: Qt5Core Qt5Gui Qt5Multimedia[+libqgsttools_p] gstreamer0.10
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstmediacapture.so
# R: Qt5Core Qt5Multimedia[+libqgsttools_p] gstreamer0.10
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstmediaplayer.so

%files -n Qt5Multimedia-gstreamer-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqgsttools_p.so
%{_libdir}/libqgsttools_p.prl
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_CameraBinServicePlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerAudioDecoderServicePlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerCaptureServicePlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerPlayerServicePlugin.cmake

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
