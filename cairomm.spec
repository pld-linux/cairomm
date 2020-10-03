#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	C++ wrapper for cairo
Summary(pl.UTF-8):	Interfejs C++ do cairo
Name:		cairomm
Version:	1.14.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://www.cairographics.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	fbcaad2d3756b42592fe8c92b39945f5
URL:		https://www.cairographics.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.12.0
BuildRequires:	doxygen >= 1:1.8.9
BuildRequires:	graphviz
BuildRequires:	libsigc++-devel >= 1:2.6.0
BuildRequires:	libstdc++-devel >= 6:4.6
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cairo >= 1.12.0
Requires:	libsigc++ >= 1:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrapper for cairo.

%description -l pl.UTF-8
Interfejs C++ do cairo.

%package devel
Summary:	Development files for cairomm library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki cairomm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.12.0
Requires:	libsigc++-devel >= 1:2.6.0
Requires:	libstdc++-devel >= 6:4.6

%description devel
Development files for cairomm library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki cairomm.

%package static
Summary:	Static cairomm library
Summary(pl.UTF-8):	Statyczna biblioteka cairomm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cairomm library.

%description static -l pl.UTF-8
Statyczna biblioteka cairomm.

%package apidocs
Summary:	cairomm API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki cairomm
Group:		Documentation
%{?noarchpackage}

%description apidocs
API and internal documentation for cairomm library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki cairomm.

%prep
%setup -q

%build
mm-common-prepare --copy --force
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcairomm-1.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libcairomm-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairomm-1.0.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairomm-1.0.so
%{_libdir}/cairomm-1.0
%{_includedir}/cairomm-1.0
%{_pkgconfigdir}/cairomm-1.0.pc
%{_pkgconfigdir}/cairomm-ft-1.0.pc
%{_pkgconfigdir}/cairomm-pdf-1.0.pc
%{_pkgconfigdir}/cairomm-png-1.0.pc
%{_pkgconfigdir}/cairomm-ps-1.0.pc
%{_pkgconfigdir}/cairomm-svg-1.0.pc
%{_pkgconfigdir}/cairomm-xlib-1.0.pc
%{_pkgconfigdir}/cairomm-xlib-xrender-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcairomm-1.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/cairomm-1.0
%{_datadir}/devhelp/books/cairomm-1.0
