
%define	_realname	orange

Summary:	SynCE Orange - a tool capable to get installable MS Cabinet Files from installers
Summary(pl.UTF-8):	SynCE Orange - narzędzie zdolne do wydobycia plików MS Cabinet z instalatorów
Name:		synce-%{_realname}
Version:	0.4
Release:	1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/synce/lib%{_realname}-%{version}.tar.gz
# Source0-md5:	40e9ac3de389c74a60007f7493e072a5
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-dynamite-libs-devel
BuildRequires:	synce-libsynce-devel
BuildRequires:	synce-unshield-libs-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orange is a tool for squeezing out juicy installable Microsoft Cabinet
Files from self-extracting installers for Microsoft Windows and some
other installer file formats.

%description -l pl.UTF-8
Orange jest narzędziem umożliwiającym wydobycie z samorozpakowujących
się instalatorów przeznaczonych dla Microsoft Windows plików Microsoft
Cabinet.

%package libs
Summary:	The Orange library
Summary(pl.UTF-8):	Biblioteka Orange
Group:		Libraries

%description libs
The Orange library.

%description libs -l pl.UTF-8
Biblioteka Orange.

%package libs-devel
Summary:	Header files for the Orange library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Orange
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files for the Orange library.

%description libs-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Orange.

%package libs-static
Summary:	Static Orange library
Summary(pl.UTF-8):	Statyczna biblioteka Orange
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static Orange library.

%description libs-static -l pl.UTF-8
Statyczna biblioteka Orange.

%prep
%setup -q -n lib%{_realname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/orange.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborange.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liborange.so.?

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborange.so
%{_libdir}/liborange.la
%{_pkgconfigdir}/liborange.pc
%{_includedir}/liborange.h
%{_includedir}/liborange_stub.h

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/liborange.a
