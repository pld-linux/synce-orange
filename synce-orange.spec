%define		pkgname	orange
Summary:	SynCE Orange - a tool capable to get installable MS Cabinet Files from installers
Summary(pl.UTF-8):	SynCE Orange - narzędzie zdolne do wydobywania plików MS Cabinet z instalatorów
Name:		synce-%{pkgname}
Version:	0.4
Release:	7
License:	MIT
Group:		Applications/File
Source0:	http://downloads.sourceforge.net/synce/lib%{pkgname}-%{version}.tar.gz
# Source0-md5:	40e9ac3de389c74a60007f7493e072a5
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.4
BuildRequires:	gettext-tools
BuildRequires:	libgsf-devel
BuildRequires:	libmagic-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-core-lib-devel >= 0.9.1
BuildRequires:	synce-dynamite-libs-devel >= 0.1
BuildRequires:	synce-unshield-libs-devel >= 0.5
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orange is a tool for squeezing out juicy installable Microsoft Cabinet
Files from self-extracting installers for Microsoft Windows and some
other installer file formats.

%description -l pl.UTF-8
Orange jest narzędziem umożliwiającym wydobywanie plików Microsoft
Cabinet z samorozpakowujących się instalatorów przeznaczonych dla
Microsoft Windows.

%package libs
Summary:	The Orange library
Summary(pl.UTF-8):	Biblioteka Orange
Group:		Libraries
Requires:	synce-core-lib >= 0.9.1
Requires:	synce-dynamite-libs >= 0.1
Requires:	synce-unshield-libs >= 0.5

%description libs
The Orange library.

%description libs -l pl.UTF-8
Biblioteka Orange.

%package libs-devel
Summary:	Header files for the Orange library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Orange
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	synce-dynamite-libs-devel >= 0.1
Requires:	synce-core-lib-devel >= 0.9.1
Requires:	synce-unshield-libs-devel >= 0.5

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
%setup -q -n lib%{pkgname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-inno \
	--enable-msi \
	--enable-vise \
	--with-libgsf

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liborange.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE TODO
%attr(755,root,root) %{_bindir}/orange
%{_mandir}/man1/orange.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborange.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liborange.so.0

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborange.so
%{_pkgconfigdir}/liborange.pc
%{_includedir}/liborange.h
%{_includedir}/liborange_stub.h

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/liborange.a
