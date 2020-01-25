#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	MatrixReal
Summary:	Math::MatrixReal - implements the data type "matrix of reals"
Summary(pl.UTF-8):	Math::MatrixReal - implementacja typu danych "macierz liczb rzeczywistych"
Name:		perl-Math-MatrixReal
Version:	2.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	67f23122424830b5eea044f987b892b9
URL:		http://search.cpan.org/dist/Math-MatrixReal/
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

%description -l pl.UTF-8
Ten moduł jest implementacją typu danych "macierz liczb rzeczywistych"
(i w konsekwencji także "wektor liczb rzeczywistych"), który może być
używany prawie tak samo jak każdy inny podstawowy typ Perla dzięki
przeciążaniu operatorów - tzn. "$product = $matrix1 * $matrix2;" zrobi
to, czego się oczekuje (pomnoży macierze).

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

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Math/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS GOALS README TODO
%{perl_vendorlib}/Math/MatrixReal.pm
%{perl_vendorlib}/Math/funcs.pl
%{_mandir}/man3/Math::Kleene.3pm*
%{_mandir}/man3/Math::MatrixReal.3pm*
