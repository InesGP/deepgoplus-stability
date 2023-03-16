import sigdigits
import sys
import numpy as np

if __name__ == '__main__':
    xf = sys.argv[-1]
    x = np.load(xf, allow_pickle=True)
    #ref = np.array([2, -2])
    ref = np.load(sys.argv[2], allow_pickle=True)
    #print(np.array(ref))
    
    sig_file = open(sys.argv[1], 'w')
    for j, r in zip (x.values(), ref):
        print(j.shape, r.shape)
        j = np.concatenate(j).reshape(10,-1).astype(np.float32)
        #r = r[0].reshape(-1).astype(np.float32)
        r = r.astype(np.float32)
        print(j.shape,type(j),r.shape, type(r))
        sig_file.write('\nNEW PROTEIN')

        for method in sigdigits.Method:
            for precision in sigdigits.Precision:
                sig = sigdigits.significant_digits(
                    j, r, precision=precision, method=method)
                sig_file.write(f"\n[{method.name:7}] {precision.name:9} significant:\n")
                for i in sig:
                    sig_file.write(str(i) + ',')
                #print(f"[{method.name:7}] {precision.name:9} significant:", sig)
                sig = sigdigits.significant_digits(
                    j, r, precision=precision, method=method, base=10)
                sig_file.write(f"\n[{method.name:7}] {precision.name:9} significant:\n")
                for i in sig: sig_file.write(str(i) + ',')
                #print(f"[{method.name:7}] {precision.name:9} significant:", sig)

            for precision in sigdigits.Precision:
                con = sigdigits.contributing_digits(
                    j, r, precision=precision, method=method)
                sig_file.write(f"\n[{method.name:7}] {precision.name:8} contributing:\n")
                for i in con: sig_file.write(str(i) + ',')
                #print(f"[{method.name:7}] {precision.name:8} contributing:", con)
                con = sigdigits.contributing_digits(
                    j, r, precision=precision, method=method, base=10)
                sig_file.write(f"\n[{method.name:7}] {precision.name:8} contributing:\n")
                for i in con: sig_file.write(str(i) + ',')
                #print(f"[{method.name:7}] {precision.name:8} contributing:", con)

    sig_file.close()
