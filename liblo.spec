Summary:	Open Sound Control library
Summary(pl):	Biblioteka Open Sound Control
Name:		liblo
Version:	0.18
Release:	1
License:	GPL v.2
Group:		Libraries
Source0:	http://plugin.org.uk/liblo/releases/%{name}-%{version}.tar.gz
# Source0-md5:	05bd26d1ebc34275cc6962183e6907fb
URL:		http://plugin.org.uk/liblo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liblo is an implementation of the Open Sound Control protocol for
POSIX systems.

%description -l pl
liblo jest implementacj± protoko³u Open Sound Control dla systemów
POSIX.

%package devel
Summary:	Header files for liblo
Summary(pl):	Pliki nag³ówkowe dla liblo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for liblo.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja dla liblo.

%package static
Summary:	liblo static library
Summary(pl):	Biblioteka statyczna liblo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
liblo static library.

%description static -l pl
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
