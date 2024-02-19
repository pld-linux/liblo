#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Open Sound Control library
Summary(pl.UTF-8):	Biblioteka Open Sound Control
Name:		liblo
Version:	0.32
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/liblo/%{name}-%{version}.tar.gz
# Source0-md5:	a93a7a9da084e6a0937bde6fc324a52a
Patch0:		%{name}-strncpy.patch
URL:		https://liblo.sourceforge.net/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liblo is an implementation of the Open Sound Control protocol for
POSIX systems.

%description -l pl.UTF-8
liblo jest implementacją protokołu Open Sound Control dla systemów
POSIX.

%package devel
Summary:	Header files for liblo
Summary(pl.UTF-8):	Pliki nagłówkowe dla liblo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for liblo.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla liblo.

%package static
Summary:	liblo static library
Summary(pl.UTF-8):	Biblioteka statyczna liblo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
liblo static library.

%description static -l pl.UTF-8
Biblioteka statyczna liblo.

%package apidocs
Summary:	API documentation for liblo library
Summary(pl.UTF-8):	Dokumentacja API biblioteki liblo
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for liblo library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki liblo.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-ipv6 \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblo.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/oscdump
%attr(755,root,root) %{_bindir}/oscsend
%attr(755,root,root) %{_bindir}/oscsendfile
%attr(755,root,root) %{_libdir}/liblo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblo.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblo.so
%{_includedir}/lo
%{_pkgconfigdir}/liblo.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liblo.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
