Summary:	Open Sound Control library
Summary(pl.UTF-8):	Biblioteka Open Sound Control
Name:		liblo
Version:	0.24
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.ecs.soton.ac.uk/~njh/liblo/%{name}-%{version}.tar.gz
# Source0-md5:	a9b5e7c6fcc835cd468e26cc95aba91a
URL:		http://plugin.org.uk/liblo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO 
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/lo
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
