module covariance
    use, intrinsic:: iso_c_binding, only: c_int
    use comm,only: sp
    !use perf, only : sysclock2ms
    Implicit none
    private
    public::autocov

contains

subroutine autocov(x,N,M,C) bind(c)
! autocovariance estimate of 1-D vector (e.g. noisy sinusoid)
! input:
! x is a 1-D vector
! N is length of x
! M is the size of signal block (integer)
! output:
! C is the 2-D result

 integer(c_int), intent(in) :: M,N
 real(sp),intent(in) :: x(N)
 real(sp),intent(out):: C(M,M)

 integer(c_int) :: i
 real(sp) :: yn(M,1), R(M,M) !, work(M,M)

 yn(:,1) = x(M:1:-1) ! index from M to 1, reverse order

 R = matmul(yn,(transpose(yn)))
 
 do i = 2, N-M ! not concurrent
    yn(:,1) = x(M-1+i:i-1:-1)
    R = R + matmul(yn,(transpose(yn)))
 enddo

 C = R/real(N,sp)

end subroutine autocov

end module covariance
