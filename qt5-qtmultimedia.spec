#
# Conditional build:
%bcond_without	doc	# Documentation
%bcond_without	qm	# QM translations

%define		orgname		qtmultimedia
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		5.9
Summary:	The Qt5 Multimedia libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Multimedia
Name:		qt5-%{orgname}
Version:	5.15.4
Release:	1
License:	LGPL v3 or GPL v2 or GPL v3 or commercial
Group:		X11/Libraries
Source0:	http://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	61eb0bb13bdf03f4e31cfb916719a86e
Source1:	http://download.qt.io/official_releases/qt/5.15/%{version}/submodules/qttranslations-everywhere-opensource-src-%{version}.tar.xz
# Source1-md5:	6ba46a712a698118f396f78a785f6774
URL:		https://www.qt.io/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
BuildRequires:	Qt5Xml-devel >= %{qtbase_ver}
BuildRequires:	alsa-lib-devel >= 1.0.10
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-gl-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	pulseaudio-devel >= 0.9.11
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
BuildRequires:	qt5-doc-common >= %{qttools_ver}
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
Requires:	alsa-lib >= 1.0.10
Requires:	pulseaudio-libs >= 0.9.11
Obsoletes:	qt5-qtmultimedia < 5.2.0-1

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
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Multimedia = %{version}-%{release}
Obsoletes:	qt5-qtmultimedia-devel < 5.2.0-1

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
Requires:	pulseaudio-devel >= 0.9.11

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
Requires:	alsa-lib-devel >= 1.0.10
Requires:	gstreamer-devel
Requires:	gstreamer-gl-devel
Requires:	gstreamer-plugins-base-devel
Requires:	pulseaudio-devel >= 0.9.11

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
BuildArch:	noarch

%description doc
Qt5 Multimedia documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Multimedia w formacie HTML.

%package doc-qch
Summary:	Qt5 Multimedia documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Multimedia w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 Multimedia documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Multimedia w formacie QCH.

%package examples
Summary:	Qt5 Multimedia examples
Summary(pl.UTF-8):	Przykłady do bibliotek Qt5 Multimedia
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 Multimedia examples.

%description examples -l pl.UTF-8
Przykłady do bibliotek Qt5 Multimedia.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version} %{?with_qm:-a1}

%build
qmake-qt5

%{__make}
%{?with_doc:%{__make} docs}

%if %{with qm}
cd qttranslations-everywhere-src-%{version}
qmake-qt5
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%if %{with qm}
%{__make} -C qttranslations-everywhere-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only qtmultimedia
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{assistant,designer,linguist,qt,qtbase,qtconnectivity,qtdeclarative,qtlocation,qtquickcontrols,qtquickcontrols2,qtserialport,qtscript,qtwebengine,qtwebsockets,qtxmlpatterns}_*.qm
%endif

# kill unnecessary -L%{_libdir} from *.la, *.prl, *.pc
%{__sed} -i -e "s,-L%{_libdir} \?,,g" \
	$RPM_BUILD_ROOT%{_libdir}/*.{la,prl} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
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
%doc LICENSE.GPL3-EXCEPT dist/changes-*
# R: Qt5Core Qt5Gui Qt5Network pulseaudio-libs
%attr(755,root,root) %{_libdir}/libQt5Multimedia.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Multimedia.so.5
%dir %{qt5dir}/plugins/audio
# R: Qt5Core Qt5Multimedia alsa-lib
%attr(755,root,root) %{qt5dir}/plugins/audio/libqtaudio_alsa.so
# R: Qt5Core Qt5Multimedia pulseaudio-libs
# (not splitting as libQt5Multimedia itself is linked with libpulse)
%attr(755,root,root) %{qt5dir}/plugins/audio/libqtmedia_pulse.so
%dir %{qt5dir}/plugins/mediaservice
%dir %{qt5dir}/plugins/playlistformats
# R: Qt5Core Qt5Multimedia Qt5Network
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
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QAlsaPlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QM3uPlaylistPlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QPulseAudioPlugin.cmake
%{qt5dir}/mkspecs/modules/qt_lib_multimedia.pri
%{qt5dir}/mkspecs/modules/qt_lib_multimedia_private.pri

%files -n Qt5MultimediaQuick
%defattr(644,root,root,755)
# R: Qt5Core Qt5Gui Qt5Multimedia Qt5Quick
%attr(755,root,root) %{_libdir}/libQt5MultimediaQuick.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5MultimediaQuick.so.5
%dir %{qt5dir}/qml/QtAudioEngine
# R: Qt5Core Qt5Gui Qt5Multimedia Qt5Qml OpenAL
%attr(755,root,root) %{qt5dir}/qml/QtAudioEngine/libdeclarative_audioengine.so
%{qt5dir}/qml/QtAudioEngine/plugins.qmltypes
%{qt5dir}/qml/QtAudioEngine/qmldir
%dir %{qt5dir}/qml/QtMultimedia
# R: Qt5Core Qt5Gui Qt5Multimedia Qt5MultimediaQuick Qt5Network Qt5Qml Qt5Quick
%attr(755,root,root) %{qt5dir}/qml/QtMultimedia/libdeclarative_multimedia.so
%{qt5dir}/qml/QtMultimedia/Video.qml
%{qt5dir}/qml/QtMultimedia/plugins.qmltypes
%{qt5dir}/qml/QtMultimedia/qmldir

%files -n Qt5MultimediaQuick-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5MultimediaQuick.so
%{_libdir}/libQt5MultimediaQuick.prl
%{_libdir}/cmake/Qt5MultimediaQuick
%{_includedir}/qt5/QtMultimediaQuick
%{qt5dir}/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri

%files -n Qt5MultimediaWidgets
%defattr(644,root,root,755)
# R: Qt5Core Qt5Gui Qt5Multimedia Qt5Widgets OpenGL
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
# R: Qt5Core Qt5Gui Qt5Multimedia Qt5MultimediaWidgets Qt5Network Qt5Widgets alsa-lib glib2 gstreamer gstreamer-gl gstreamer-plugins-base
%attr(755,root,root) %{_libdir}/libQt5MultimediaGstTools.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5MultimediaGstTools.so.5
%{_libdir}/cmake/Qt5MultimediaGstTools
# R: Qt5Core Qt5Multimedia Qt5MultimediaGstTools glib2 gstreamer gstreamer-plugins-base
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstaudiodecoder.so
# R: Qt5Core Qt5Gui Qt5Multimedia Qt5MultimediaGstTools glib2 gstreamer gstreamer-plugins-base
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstcamerabin.so
# R: Qt5Core Qt5Gui Qt5Multimedia Qt5MultimediaGstTools glib2 gstreamer gstreamer-plugins-base
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstmediacapture.so
# R: Qt5Core Qt5Multimedia Qt5MultimediaGstTools gstreamer
%attr(755,root,root) %{qt5dir}/plugins/mediaservice/libgstmediaplayer.so

%files -n Qt5Multimedia-gstreamer-devel
%defattr(644,root,root,755)
%{_includedir}/qt5/QtMultimediaGstTools
%attr(755,root,root) %{_libdir}/libQt5MultimediaGstTools.so
%{qt5dir}/mkspecs/modules/qt_lib_multimediagsttools_private.pri
%{_libdir}/libQt5MultimediaGstTools.prl
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_CameraBinServicePlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerAudioDecoderServicePlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerCaptureServicePlugin.cmake
%{_libdir}/cmake/Qt5Multimedia/Qt5Multimedia_QGstreamerPlayerServicePlugin.cmake

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtmultimedia

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtmultimedia.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
