#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	MatrixReal
Summary:	Math::MatrixReal - implements the data type "matrix of reals"
Summary(pl):	Math::MatrixReal - implementacja typu danych "macierz liczb rzeczywistych"
Name:		perl-Math-MatrixReal
Version:	1.9
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4df6e63d0e9ff902f1af5dc430a0b483
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implements the data type "matrix of reals" (and consequently also
"vector of reals"), which can be used almost like any other basic Perl
type thanks to OPERATOR OVERLOADING, i.e., "$product = $matrix1 *
$matrix2;" does what you would like it to do (a matrix
multiplication).

%description -l pl
Ten modu� jest implementacj� typu danych "macierz liczb rzeczywistych"
(i w konsekwencji tak�e "wektor liczb rzeczywistych"), kt�ry mo�e by�
u�ywany prawie tak samo jak ka�dy inny podstawowy typ Perla dzi�ki
przeci��aniu operator�w - tzn. "$product = $matrix1 * $matrix2;" zrobi
to, czego si� oczekuje (pomno�y macierze).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/*
%{_mandir}/man3/*
