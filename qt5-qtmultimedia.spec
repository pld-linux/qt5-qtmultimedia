# TODO:
# - cleanup

%define		orgname		qtmultimedia
Summary:	The Qt5 Multimedia
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
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	qt5-qttools-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

%description
Qt5 Multimedia libraries.

%package devel
Summary:	The Qt5 Multimedia - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Qt5 Multimedia - development files.

%package doc
Summary:	The Qt5 Multimedia - docs
Group:		Documentation

%description doc
Qt5 Multimedia - documentation.

%package examples
Summary:	Qt5 Multimedia examples
Group:		X11/Development/Libraries

%description examples
Qt5 Multimedia - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

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

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Multimedia.so.?
%attr(755,root,root) %{_libdir}/libQt5Multimedia.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5MultimediaQuick_p.so.?
%attr(755,root,root) %{_libdir}/libQt5MultimediaQuick_p.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5MultimediaWidgets.so.?
%attr(755,root,root) %{_libdir}/libQt5MultimediaWidgets.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libqgsttools_p.so.?
%attr(755,root,root) %{_libdir}/libqgsttools_p.so.*.*
%attr(755,root,root) %{_qtdir}/plugins
%{_qtdir}/qml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Multimedia.so
%attr(755,root,root) %{_libdir}/libQt5MultimediaQuick_p.so
%attr(755,root,root) %{_libdir}/libQt5MultimediaWidgets.so
%attr(755,root,root) %{_libdir}/libqgsttools_p.so

%{_libdir}/libQt5Multimedia.la
%{_libdir}/libQt5MultimediaQuick_p.la
%{_libdir}/libQt5MultimediaWidgets.la

%{_libdir}/libQt5Multimedia.prl
%{_libdir}/libQt5MultimediaQuick_p.prl
%{_libdir}/libQt5MultimediaWidgets.prl
%{_libdir}/libqgsttools_p.prl

%{_libdir}/cmake/Qt5Multimedia
%{_libdir}/cmake/Qt5MultimediaWidgets
%{_includedir}/qt5/QtMultimedia
%{_includedir}/qt5/QtMultimediaQuick_p
%{_includedir}/qt5/QtMultimediaWidgets
%{_pkgconfigdir}/*.pc
%{_qtdir}/mkspecs

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc

%files examples -f examples.files
